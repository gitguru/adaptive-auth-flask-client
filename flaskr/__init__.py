import datetime
import time
import os

from flask import Flask


def _jinja2_filter_datetime(unix_timestamp):
    # return time.ctime(date)
    # return datetime.datetime.utcfromtimestamp(posix_time).strftime('%Y-%m-%dT%H:%M:%SZ')
    # return time.gmtime(unix_timestamp)
    return datetime.datetime.fromtimestamp(unix_timestamp / 1000)




def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    # a simple page that says hello
    # @app.route('/hello')
    # def hello():
        # return 'Hello, World!'
    from . import flask_demo
    app.register_blueprint(flask_demo.bp)
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/error', endpoint='error')

    # allow to format unix timestamp in jinja2 templates
    # app.add_template_filter('ctime', _jinja2_filter_datetime)
    app.jinja_env.filters['ctime'] = _jinja2_filter_datetime


    return app