# coding=utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

from flask import current_app, request, redirect, url_for, Blueprint
from sanction import Client

from hocus_focus.csrf import csrf


core = Blueprint('core', __name__)
oauth = Blueprint('oauth', __name__)
blueprints = [core, oauth]

OAUTH_REDIRECT_URI = 'https://hocus-focus.herokuapp.com/login/github/'
# url_for('oauth.finish_github_login', _external=True)
GITHUB_AUTH_ENDPOINT = 'https://github.com/login/oauth/authorize'
GITHUB_TOKEN_ENDPOINT = 'https://github.com/login/oauth/access_token'
GITHUB_RESOURCE_ENDPOINT = 'https://api.github.com'
GITHUB_SCOPE = ''  # Public read-only access


@core.route('/health/')
def index():
    return "Hello Heroku Whiskey!"


@oauth.before_request
def adapt_oauth_state_to_normal_csrf():
    view_func = current_app.view_functions.get(request.endpoint)
    if view_func is not finish_github_login:
        return
    # We manipulate stuff at the WSGI level here because the Werkzeug equivalents are annoyingly immutable.
    request.environ[b'REQUEST_METHOD'] = b'POST'  # pretend it's not GET so that it becomes CSRF-protected
    try:
        csrf_token = request.args['state']
    except KeyError:
        return
    request.environ[b'HTTP_' + csrf._csrf_header_name.encode('ascii')] = csrf_token


@oauth.route('/login/')
def start_github_login():
    c = Client(
        auth_endpoint=GITHUB_AUTH_ENDPOINT,
        client_id=current_app.config['GITHUB_OAUTH_CLIENT_ID'],
    )
    return redirect(c.auth_uri(scope=GITHUB_SCOPE, state=csrf._get_token(), redirect_uri=OAUTH_REDIRECT_URI))


@oauth.route('/login/github/', methods=['GET', 'POST'])
def finish_github_login():
    c = Client(token_endpoint=GITHUB_TOKEN_ENDPOINT,
        resource_endpoint=GITHUB_RESOURCE_ENDPOINT,
        client_id=current_app.config['GITHUB_OAUTH_CLIENT_ID'],
        client_secret=current_app.config['GITHUB_OAUTH_CLIENT_SECRET'],
    )
    c.request_token(code=request.args['code'], redirect_uri=OAUTH_REDIRECT_URI)
    user_data = c.request('/user')
    print("USER:", repr(user_data))
    return "Hello person!"
    # 'name', 'login', 'avatar_url'
