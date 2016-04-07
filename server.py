#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import run, static_file, get
import settings

# import controllers
from controllers import *


@get('/') # prefer nginx
def index():
    return static_file("index.html", root='./front')


@get('/front/<path:path>')  # prefer nginx
def front(path):
    return static_file(path, root='./front')


@get('/robots.txt')
def robots():
    return static('robots.txt')


if __name__ == "__main__":
    run(**settings.SERVER)
