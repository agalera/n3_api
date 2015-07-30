#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from bottle import run, static_file, get, post, request, redirect, response
from jinja2 import Environment, FileSystemLoader, FileSystemBytecodeCache
import settings

# import views
from views.admin import Admin
from views.news import News
from views.about import About


@get('/static/<path:path>')  # prefer nginx
def static(path):
    return static_file(path, root='./static')


@get('/robots.txt')
def robots():
    return static('robots.txt')


if __name__ == "__main__":
    run(**settings.SERVER)
