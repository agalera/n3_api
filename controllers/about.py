from bottle import get
from modules.render import draw


class About:

    @get('/about')
    def about(*args, **kwargs):
        return draw(view='about', title="About")
