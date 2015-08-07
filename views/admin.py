from bottle import get, post, request, redirect
from modules.render import draw
from modules.oauth2 import auth
from models.admin import M_admin


class Admin:
    @get('/admin')
    @auth(1)
    def admin(*args, **kwargs):
        return draw(view='admin', title="Admin")

    # interacts with the database

    @post('/new_post')
    @auth(1)
    def new_post(*args, **kwargs):
        new_id = M_admin.new_post(kwargs['n3_token']['id'],
                                  request.forms.get('title').decode('utf-8'),
                                  request.forms.get('texto').decode('utf-8'),
                                  request.forms.get('tags').split(','),
                                  request.environ.get('REMOTE_ADDR'))
        return redirect('/comments/' + str(new_id))
