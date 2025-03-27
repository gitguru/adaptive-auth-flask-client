from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app as app

from flaskr.service import demo_server_api_service
from flaskr.service import client_id_service
from flaskr.service import totp_service

# initialize flask demo blue print (view)
bp = Blueprint('flask_demo', __name__, url_prefix='/')


@bp.route('/', methods=('GET',))
def index():
    api_client = client_id_service.get_current_api_client()
    return render_template('index.html', api_client=api_client)


@bp.route('/settings', methods=('POST',))
def settings_save():
    if request.method == 'POST':
        client_id = request.form['clientId']
        if client_id_service.get_current_api_client():
            client_id_service.update_api_client(clientId=client_id)
        else:
            client_id_service.add_api_client(clientId=client_id)

    return redirect(url_for("index"))


def get_totp(transaction_id) -> str:
    token_type = request.args['token_type'] if 'token_type' in request.args else 'self'
    if token_type == 'self':
        return totp_service.get_self_totp_token()
    else:
        totp_token_response = totp_service.get_server_totp_token(transaction_id)
        app.logger.info('TOTP token response: %s', totp_token_response)
        if totp_token_response['status_code'] == 200:
            return totp_token_response['body']['totp']
        else:
            return totp_token_response


def resolve_totp_challenge(transaction_id: str):
    totp = get_totp(transaction_id)

    if type(totp) == str:
        validate_totp_response = demo_server_api_service.validate_client_totp(transaction_id, totp)
        app.logger.info('TOTP validatoin response: %s', validate_totp_response)
        if validate_totp_response['status_code'] == 200:
            return timestamp()
        else:
            return render_template('error.html', error=validate_totp_response)
    else:
        return render_template('error.html', error=totp)


@bp.route('/timestamp', methods=('GET',))
def timestamp():
    
    timestamp_response = demo_server_api_service.get_timestamp()
    app.logger.info('Timestamp response: %s', timestamp_response)

    if timestamp_response['status_code'] == 200:
        timestamp = timestamp_response['body']['timestamp']
        return render_template('timestamp.html', timestamp=timestamp)

    if timestamp_response['status_code'] == 401:
        tid = timestamp_response['body']['transaction_id']
        return resolve_totp_challenge(tid)

    return render_template('error.html', error=timestamp_response)
