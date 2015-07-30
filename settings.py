SECRET = "n3isgood"

MONGODB = {'HOSTS': ['localhost'],
           'DBNAME': 'blog'}


GUNICORN = {'server': 'gunicorn', 'host': '0.0.0.0', 'port': 9999,
            'workers': 1, 'worker_class': 'eventlet', 'debug': False,
            'reloader': False}

DEFAULT = {'host': '0.0.0.0', 'port': 9999, 'debug': True, 'reloader': True}

SERVER = GUNICORN

COOKIE_NAME = 'n3_token'
JINJA2_CACHE = '/home/common/tmp/jinjacache'
oauth2g = {"auth_uri": "https://accounts.google.com/o/oauth2/auth",
           "client_secret": "XXXX",
           "token_uri": "https://accounts.google.com/o/oauth2/token",
           "client_email": "XXXX@developer.gserviceaccount.com",
           "redirect_uris": ["http://yourdomain.com"],
           "client_x509_cert_url": "XXXX",
           "client_id": "XXXXXXXXXXXXX",
           "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
           "javascript_origins": ["https://XXXXXXXXXXXXX"],
           "name": "XXXXXXXXXXXX"}
