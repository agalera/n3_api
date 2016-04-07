from bottle import post, request, redirect
from modules.oauth2 import auth
from models.admin import M_admin


class Admin:
    @post('/new_post')
    @auth(1)
    def new_post(auth_user):
        new_id = M_admin.new_post(kwargs['auth_user']['id'],
                                  request.forms.get('title').decode('utf-8'),
                                  request.forms.get('texto').decode('utf-8'),
                                  request.forms.get('tags').split(','),
                                  request.environ.get('REMOTE_ADDR'))
        return {'result': True, 'id': new_id}
