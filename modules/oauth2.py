from bottle import get, redirect, response, request, HTTPError, tob, _lscmp
from models.login import M_login
import rauth
import settings
import json
import functools
import hashlib
import base64
import hmac

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


def cookie_encode(data, key=settings.SECRET, digestmod=None):
    """ Encode and sign a json object. Return a (byte) string """
    digestmod = digestmod or hashlib.sha256
    msg = base64.b64encode(json.dumps(data, -1))
    sig = base64.b64encode(hmac.new(tob(key),
                           msg, digestmod=digestmod).digest())
    return tob('!') + sig + tob('?') + msg


def cookie_decode(data, key=settings.SECRET, digestmod=None):
    """ Verify and decode an encoded string. Return an object or None."""
    data = tob(data)
    sig, msg = data.split(tob('?'), 1)
    digestmod = digestmod or hashlib.sha256
    hashed = hmac.new(tob(key), msg, digestmod=digestmod).digest()
    if _lscmp(sig[1:], base64.b64encode(hashed)):
        return json.loads(base64.b64decode(msg))
    return None


def get_cookie(param=None):
    params = cookie_decode(request.get_cookie(settings.COOKIE_NAME))
    if params is None:
        return None

    if param is None:
        return params
    return params.get(param, None)


def auth(check):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*a, **ka):
            token = get_cookie()
            ka['auth_user'] = token
            print token
            if token is not None and token['account_type'] < check:
                user = M_login.get_user(token['_id'])
                if user['account_type'] == token['account_type']:
                    return func(*a, **ka)
                print '**************** hacked info ****************'
                print token
                print '**************** hacked end ****************'
            return HTTPError(403, "Forbbiden")
        return wrapper
    return decorator


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
    session_json['_id'] = session_json['id']
    session_json = M_login.check_user(session_json)  # create user if not exist
    response.set_cookie(settings.COOKIE_NAME,
                        cookie_encode(session_json, settings.SECRET))

    return redirect("/")


def remove_cookies():
    response.delete_cookie(settings.COOKIE_NAME)


@get('/logout')
def logout():
    remove_cookies()
    return redirect("/")
