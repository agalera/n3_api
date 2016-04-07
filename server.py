#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import run, static_file, get
import settings

# import controllers
from controllers import *

if settings.STATIC_FILES:
    @get('/')
    def index():
        return static('index.html')

    @get('/<path:path>')
    def static(path):
        return static_file(path, root='./front')


if __name__ == "__main__":
    run(**settings.SERVER)
