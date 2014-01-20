# coding=utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

from hocus_focus.app_factory import create_app


app = create_app()
application = app.wsgi_app
