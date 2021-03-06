# coding=utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

import os
import logging

from flask import Flask

from hocus_focus.models import db
from hocus_focus.csrf import csrf
from hocus_focus.routes import blueprints


CONFIG_KEYS = {
    'SECRET_KEY',
    'GITHUB_OAUTH_CLIENT_ID',
    'GITHUB_OAUTH_CLIENT_SECRET',
}


def create_app():
    app = Flask(__name__)
    app.config.update({key: os.environ[key.encode('ascii')] for key in CONFIG_KEYS})
    app.config['PREFERRED_URL_SCHEME'] = b'https'
    app.config['SESSION_COOKIE_SECURE'] = app.config['CSRF_COOKIE_SECURE'] = app.config['CSRF_COOKIE_HTTPONLY'] = True

    app.logger.setLevel(logging.DEBUG)  # FIXME
    app.logger.addHandler(logging.StreamHandler())

    csrf.init_app(app)
    db.init_app(app)

    # principals = Principal()
    # principals.init_app(app)

    for blueprint in blueprints:
        app.register_blueprint(blueprint)  # url_prefix="/web"

    return app
