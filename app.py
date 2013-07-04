#!/usr/bin/env python

import logging
from bottle import route, run, template, static_file

logging.basicConfig(format = '%(asctime)-15s %(message)s', level = logging.DEBUG)


def render_page(body, **kwargs):
    return str(template('templates/base', **kwargs))

@route('/', method = 'GET')
def index():
    body = template('templates/index')
    return render_page(body)

@route('<path:re:/static/css/.*css>')
@route('<path:re:/static/js/.*js>')
def static(path, method = 'GET'):
    return static_file(path, root = '.')


