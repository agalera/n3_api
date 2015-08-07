from bottle import get, post, request, redirect
from modules.render import draw
from modules.oauth2 import auth, get_cookie
from models.news import M_news
import settings


class News:

    @get('/')
    @get('/news')
    @get('/other_news/<page>')
    def other_news(page=0, *args, **kwargs):
        return draw(view='news', title="Home", tot={'news': M_news.news(int(page))},
                    **kwargs)

    @get('/search/page/<page>/tags/<tags:path>')
    def view_tags(tags, page, *args, **kwargs):
        tags_parse = tags.split('/')
        return draw(view='news',
                    title="Search tags",
                    tot={'news': M_news.tags(tags_parse, int(page)),
                         'tags': tags_parse,
                         'tags_parse': tags_parse,
                         'search': True},
                    **kwargs)

    @get('/comments/<id_post>')
    def comments(id_post, *args, **kwargs):
        tot = M_news.regenerate_comments(id_post)
        tot['account_type'] = get_cookie('account_type')
        return draw(view=['comments', 'add_comments'], title="Comments",
                    tot=tot, **kwargs)

    @post('/new_comment/<id_post>')
    @auth(1)
    def new_comment(id_post, *args, **kwargs):
        M_news.new_comment(id_post, request.forms.get('texto').decode(
            'utf-8'), request.environ.get('REMOTE_ADDR'), *args, **kwargs)
        return redirect('/comments/' + id_post)
