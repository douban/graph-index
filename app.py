#!/usr/bin/env python

import os
import re
import json
import pickle
from urllib import urlencode
from collections import defaultdict
from bottle import route, template, static_file, request, redirect, default_app, hook

import config
from models import Graph
from examples import examples
from utils import logging, build_metrics, build_diamond, groupby_re

logging.info('build metrics...')
metrics = build_metrics()

logging.info('build diamond...')
diamond = build_diamond(metrics)

metrics_version = os.path.getmtime(config.metrics_file)

@hook('before_request')
def check_metrics():
    global metrics, diamond, metrics_version
    if os.path.getmtime(config.metrics_file) > metrics_version:
        metrics = json.loads(open(config.metrics_file).read())
        diamond = pickle.loads(open(config.diamond_cache).read())

# web part
def render_page(body, **kwargs):
    return str(template('templates/base', body = body, **kwargs))

@route('/', method = 'GET')
@route('/index', method = 'GET')
def index():
    body = template('templates/index', **globals())
    return render_page(body)

@route('/dashboard', method = 'GET')
def dashboard():
    global diamond
    plugins = defaultdict(dict)
    for server in diamond.keys():
        prefix = re.sub('\d+$', '', server)
        for plugin in diamond[server].keys():
            plugins[plugin][prefix] = True # dict is faster than set
    body = template('templates/dashboard', **locals())
    return render_page(body, page = 'dashboard')

@route('/server/<server>', method = 'GET')
def server(server = ''):
    global diamond
    graphs = []
    for plugin in sorted(diamond[server].keys()):
        graph = Graph(diamond[server][plugin], title = server + ' ' + plugin)
        graph.detail_url = '/server/%s/%s' % (server, plugin)
        graph.detail_title = plugin
        graphs.append(graph)
    body = template('templates/graph-list', **locals())
    return render_page(body)

@route('/server/<server>/<plugin>', method = 'GET')
def plugin(server = '', plugin = ''):
    global diamond
    graph = Graph(diamond[server][plugin], title = server + ' ' + plugin)
    body = template('templates/graph', **locals())
    return render_page(body)

@route('/metric/<metric_name>', method = 'GET')
def metric(metric_name = ''):
    graph = Graph([metric_name, ])
    graph.day_graph_need_shift = True
    graph.auto_refresh = True
    body = template('templates/graph', **locals())
    return render_page(body)

@route('/regex/', method = 'GET')
@route('/regex/', method = 'POST')
def regex():
    global metrics, diamond
    errors = []
    if request.method == 'POST':
        search = request.forms.get('search')
        if not search.strip():
            errors.append('can not be none')
        else:
            return redirect('/regex/?' + urlencode({'search' : search}))
    elif request.method == 'GET':
        # url will be like '/regex/?search=...'
        search = request.query.get('search', '')
        if search.strip() in ['.*', '.*?']:
            errors.append('are you kidding me?')
        elif ':' in search: # search is started with prefix
            if search.startswith('plugin:'): # search == 'plugin:<plugin>:<server_regex>'
                _, plugin, server_regex = search.strip().split(':', 2)
                graphs = []
                data = do_plugin(diamond, plugin, server_regex)
                for server in sorted(data.keys()):
                    graph = Graph(data[server], title = server + ' ' + plugin)
                    graph.detail_url = '/server/%s/%s' % (server, plugin)
                    graphs.append(graph)
                body = template('templates/graph-list', **locals())
            elif search.startswith('merge:'): # search == 'merge:'
                _, regex = search.strip().split(':', 1)
                title = request.query.get('title')
                targets = search_metrics(metrics, regex)
                graph = Graph(targets, title = title or 'a merged graph')
                body = template('templates/graph', **locals())
            elif search.startswith('sum:'): # search == 'merge:'
                _, regex = search.strip().split(':', 1)
                targets = search_metrics(metrics, regex)
                graph = Graph(['sumSeries(%s)' % (','.join(targets)), ], title = 'a sum-ed graph')
                body = template('templates/graph', **locals())
        else: # search is common regex without any prefix
            match = groupby_re.match(search)
            if match:
                graphs = []
                for group, targets in do_groupby(metrics, **match.groupdict()):
                    graph = Graph(targets, title = group)
                    graph.detail_url = '/regex/?search=merge:^(%s)$&title=%s' % ('|'.join(graph.targets), group)
                    graph.detail_title = group
                    graphs.append(graph)
                body = template('templates/graph-list', **locals())
            else:
                data = search_metrics(metrics, search)
                if len(data) == 0:
                    errors.append('no metric is matched')
                graphs = []
                for metric in data:
                    graph = Graph(targets = [metric, ], title = metric)
                    graph.detail_url = '/metric/%s' % metric
                    graph.detail_title = metric
                    graph.auto_refresh = True
                    graphs.append(graph)
                body = template('templates/graph-list', **locals())
    if errors:
        body = template('templates/error', **locals())
    return render_page(body, search = search)

@route('/debug', method = 'GET')
def debug():
    global diamond, metrics
    plugins = defaultdict(dict) # dict is faster than set
    plugins_num = len(set(reduce(lambda x,y:x+y, [diamond[server].keys() \
        for server in diamond.keys()])))
    metrics_num = len(metrics)
    for metric in metrics:
        match_obj = diamond_re.match(metric)
        if match_obj:
            match = match_obj.groupdict()
            server = match.get('server')
            plugin = match.get('plugin')
            path = metric[len('servers.%s.%s.' % (server, plugin)):]
            plugins[plugin][path] = True
    body = template('templates/debug', **locals())
    return render_page(body, page = 'debug')

@route('<path:re:/favicon.ico>', method = 'GET')
@route('<path:re:/static/css/.*css>', method = 'GET')
@route('<path:re:/static/js/.*js>', method = 'GET')
@route('<path:re:/static/fonts/.*woff>', method = 'GET')
def static(path):
    return static_file(path, root = '.')


