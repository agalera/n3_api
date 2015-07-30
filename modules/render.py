#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import request
from modules.oauth2 import *
import settings
from jinja2 import Environment, FileSystemLoader, FileSystemBytecodeCache

bcc = FileSystemBytecodeCache(settings.JINJA2_CACHE, '%s.cache')
jinja2_env = Environment(
        loader=FileSystemLoader('templates/'), bytecode_cache=bcc)


def template(name, *args, **ctx):
    t = jinja2_env.get_template(name)
    return t.render(**ctx)


def draw(*args, **kwargs):
    username = get_cookie('name')
    template_list = [template(
        'header.tpl', title=kwargs['title'],
        section=kwargs['view'], username=username)]
    if "tot" in kwargs:
        if not isinstance(kwargs['view'], list):
            kwargs['view'] = [kwargs['view']]

        for view in kwargs['view']:
            template_list.append(
                template(view + ".tpl",
                         values={'kwargs': kwargs['tot'],
                                 'username': username}))
    else:
        template_list.append(template(kwargs['view'] + ".tpl"))

    template_list.append(template('footer.tpl'))
    return template_list
