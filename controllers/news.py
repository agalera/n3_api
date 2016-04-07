from bottle import get, post, request, redirect
from modules.oauth2 import auth, get_cookie
from models.news import M_news
import settings


class News:

    @get('/api/news')
    @get('/api/other_news/<page>')
    def other_news(page=0):
        return {'news': M_news.news(int(page))}

    @get('/api/search/page/<page>/tags/<tags:path>')
    def view_tags(page, tags):
        tags_parse = tags.split('/')
        return {'news': M_news.tags(tags_parse, int(page)),
                'tags': tags_parse,
                'search': True}

    @get('/api/comments/<id_post>')
    def comments(id_post):
        return M_news.new_detailed(id_post)

    @post('/api/new_comment/<id_post>')
    @auth(0)
    def new_comment(id_post, auth_user):
        M_news.new_comment(id_post, request.forms.get('texto').decode(
            'utf-8'), request.environ.get('REMOTE_ADDR'), auth_user)
        return {"result": True}

