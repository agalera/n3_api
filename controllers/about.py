from bottle import get
from modules.render import draw


class About:

    @get('/api/about')
    def about(*args, **kwargs):
        return draw(view='about', title="About")
