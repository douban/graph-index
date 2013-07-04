#!/usr/bin/env python

import re
import json
import logging
from bottle import route, run, template, static_file, request

logging.basicConfig(format = '%(asctime)-15s %(message)s', level = logging.DEBUG)

metrics = json.loads(open('metrics.json').read())

def find_metrics(search):
    global metrics
    matched_metrics = []
    try:
        re_obj = re.compile(search)
    except:
        return None
    for m in metrics:
        if re_obj.search(m):
            matched_metrics.append(m)
    return matched_metrics

def render_page(body, **kwargs):
    return str(template('templates/base', body = body, **kwargs))

@route('/', method = 'GET')
@route('/', method = 'POST')
def index():
    if request.method == 'POST':
        search = request.forms.get('search', None)
        if search.strip():
            matched_metrics = find_metrics(search)
    body = template('templates/index', **locals())
    return render_page(body)

@route('<path:re:/static/css/.*css>')
@route('<path:re:/static/js/.*js>')
def static(path, method = 'GET'):
    return static_file(path, root = '.')


