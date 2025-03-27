import pyotp
import base64
import requests, http.client
from flask import Flask, request
from flaskr.service import client_id_service
from flaskr import constants


def get_self_totp_token() -> str:
    secret = base64.b32encode(str.encode(client_id_service.get_current_api_client()['public_key']))
    totp = pyotp.TOTP(secret)
    return totp.now()


def get_server_totp_token(transaction_id: str) -> dict:
    headers = {**request.headers}
    headers['Accept'] = 'application/json'
    headers['Remote_Addr'] = request.remote_addr
    headers['X-API-Dynamics-Client-Id'] = client_id_service.get_current_api_client()['public_key']
    headers.pop('Host') # must remove it because requests library uses its own

    response = requests.get(f"{constants.DEMO_SERVER_BASE_URL}/adaptiveAuthentication/generateClientTotp?tid={transaction_id}", headers=headers)
    status = f"{response.status_code} - {http.client.responses[response.status_code]}"
    return {'status_code': response.status_code, 'status': status, 'body': response.json()}
