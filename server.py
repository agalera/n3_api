#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import run, static_file, get
import settings

# import controllers
from controllers import *

if settings.STATIC_FILES:
    @get('/static/<path:path>')
    def static(path):
        return static_file(path, root='./front')

    @get('/<path:path>')
    @get('/')
    def static2(path=None):
        return static_file('index.html', root='./front')


if __name__ == "__main__":
    run(**settings.SERVER)
