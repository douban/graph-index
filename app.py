#!/usr/bin/env python

import re
import json
import urllib2
import logging
from urllib import urlencode
from collections import defaultdict
from bottle import route, run, template, static_file, request, redirect

import config

logging.basicConfig(format = '%(asctime)-15s %(message)s', level = logging.DEBUG)

diamond_re = re.compile('^servers\.(?P<server>[^\.]+)\.(?P<plugin>[^\.]+)\..*$')

#metrics = json.loads(urllib2.urlopen(config.graphite_url + '/metrics/index.json').read())
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

def get_diamond():
    global metrics
    diamond = {}
    for m in metrics:
        o = diamond_re.match(m)
        if o:
            d = o.groupdict()
            if not diamond.has_key(d['server']):
                diamond[d['server']] = {}
            if not diamond[d['server']].has_key(d['plugin']):
                diamond[d['server']][d['plugin']] = []
            diamond[d['server']][d['plugin']].append(m)
    return diamond


diamond = get_diamond()


def render_page(body, **kwargs):
    return str(template('templates/base', body = body, **kwargs))

@route('/', method = 'GET')
@route('/', method = 'POST')
@route('/index', method = 'GET')
@route('/index', method = 'POST')
def index():
    global diamond
    if request.method == 'POST':
        search = request.forms.get('search', '')
        if search.strip():
            return redirect('/regex/?' + urlencode({'search':search}))
    body = template('templates/index', diamond = diamond)
    return render_page(body)

@route('/server/<server>', method = 'GET')
def plugin(server = ''):
    global diamond
    data = diamond[server]
    body = template('templates/server', **locals())
    return render_page(body)

@route('/server/<server>/<plugin>', method = 'GET')
def plugin(server = '', plugin = ''):
    global diamond
    data = diamond[server][plugin]
    body = template('templates/plugin', **locals())
    return render_page(body)

@route('/metric/<metric_name>', method = 'GET')
def metric(metric_name = ''):
    body = template('templates/metric', m = metric_name)
    return render_page(body)

@route('/regex/', method = 'GET')
def regex():
    search = request.query.get('search', '')
    matched_metrics = find_metrics(search)
    body = template('templates/graph', **locals())
    return render_page(body, search = search)

@route('<path:re:/static/css/.*css>')
@route('<path:re:/static/js/.*js>')
def static(path, method = 'GET'):
    return static_file(path, root = '.')


