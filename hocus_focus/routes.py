# coding=utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

from flask import Blueprint


core = Blueprint('core', __name__)
blueprints = [core]


@core.route('/')
def index():
    return "Hello Heroku Whiskey!"
