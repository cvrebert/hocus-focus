# coding=utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

import os
import logging

from flask import Flask

from hocus_focus.models import db
from hocus_focus.csrf import csrf
from hocus_focus.routes import blueprints


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ[b'SECRET_KEY']
    # app.config.from_object(config_obj_dotted_path)

    app.logger.setLevel(logging.DEBUG)  # FIXME
    app.logger.addHandler(logging.StreamHandler())

    csrf.init_app(app)
    db.init_app(app)

    # principals = Principal()
    # principals.init_app(app)

    for blueprint in blueprints:
        app.register_blueprint(blueprint)  # url_prefix="/web"

    return app
