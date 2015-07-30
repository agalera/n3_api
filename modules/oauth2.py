from bottle import get, redirect, response, request
from models.login import M_login
import rauth
import settings
import json


cookies_names = ['name', 'id', 'picture', 'locale', 'link', 'given_name',
                 'email', 'verified_email', 'account_type']
oauth2 = rauth.OAuth2Service
google = oauth2(
    client_id=settings.oauth2g['client_id'],
    client_secret=settings.oauth2g['client_secret'],
    name=settings.oauth2g['name'],
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    base_url='https://accounts.google.com/o/oauth2/auth',
)
redirect_uri = '{uri}/oauth2callback'.format(
    uri=settings.oauth2g['redirect_uris'][0]
)


def get_cookie(param=None):

    params = request.get_cookie(settings.COOKIE_NAME, secret=settings.SECRET)
    if params is None:
        return None
    else:
        params = json.loads(params)

    if param is None:
        return params
    else:
        try:
            return params[param]
        except:
            return None


def require_user(fn):
    def check_uid(**kwargs):
        kwargs['n3_token'] = get_cookie()
        if kwargs['n3_token'] is None:
            redirect("/login")
        return fn(**kwargs)
    return check_uid


def require_admin(fn):
    def check_uid(**kwargs):
        kwargs['n3_token'] = get_cookie()
        if kwargs['n3_token'] is None or kwargs['n3_token']['account_type'] != 1:
            redirect("/login")
        return fn(**kwargs)
    return check_uid


@get('/login<:re:/?>')
def login():
    params = dict(
        scope='email profile',
        response_type='code',
        redirect_uri=redirect_uri
    )
    url = google.get_authorize_url(**params)

    redirect(url)


@get('/oauth2callback<:re:/?>')
def login_success():
    code = request.params.get('code')
    session = google.get_auth_session(
        data=dict(
            code=code,
            redirect_uri=redirect_uri,
            grant_type='authorization_code'
        ),
        decoder=json.loads
    )
    json_path = 'https://www.googleapis.com/oauth2/v1/userinfo'
    session_json = session.get(json_path).json()
    # For non-Ascii characters to work properly!
    session_json = dict((k, unicode(v).encode('utf-8'))
                        for k, v in session_json.iteritems())
    if session_json['id'] in ['101838179005792233548']:
        session_json['account_type'] = 1
    else:
        session_json['account_type'] = 0

    M_login.update_user(session_json)
    response.set_cookie(settings.COOKIE_NAME, json.dumps(session_json),
                        secret=settings.SECRET)
    print "info session", session_json
    return redirect("/")


def remove_cookies():
    response.delete_cookie(settings.COOKIE_NAME)


@get('/logout')
def logout():
    remove_cookies()
    return redirect("/")
