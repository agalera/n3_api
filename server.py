#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import run, static_file, get
import settings

# import controllers
from controllers import *


@get('/static/<path:path>')  # prefer nginx
def static(path):
    return static_file(path, root='./static')


@get('/robots.txt')
def robots():
    return static('robots.txt')


if __name__ == "__main__":
    run(**settings.SERVER)
