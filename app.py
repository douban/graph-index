#!/usr/bin/env python

import os
import re
import sys
import json
import urllib2
import logging
import itertools
from urllib import urlencode
from collections import defaultdict
from bottle import route, template, static_file, request, redirect, default_app

import config
from models import Graph
from suggested_queries import suggested_queries

logging.basicConfig(format = '%(asctime)-15s %(message)s', level = logging.DEBUG)

diamond_re = re.compile('^servers\.(?P<server>[^\.]+)\.(?P<plugin>[^\.]+)\..*$')
diamond_re_more = re.compile('^servers\.(?P<server>[^\.]+)\.(?P<plugin>(network|iostat))\.(?P<more>[^\.]+)\..*$')
bad_metrics = [
    re.compile('^servers\.[^\.]+\.memory\.Vmalloc.*$'),
    re.compile('^servers\.[^\.]+\.processresources\.[^\.]+\.vms$'),
    re.compile('^servers\.[^\.]+\.cpu\.total\.idle$'),
]
diamond = defaultdict(dict)
groupby_re = re.compile('^(?P<search>[^ ]*)\s+group\s*by\s*(?P<index>\-?\d+)$')

def is_bad_metric(metric):
    global bad_metrics
    for r in bad_metrics:
        if r.match(metric):
            return True

def build_metrics():
    global metrics
    try:
        if os.path.exists(config.metrics_file) and config.debug:
            data = open(config.metrics_file).read()
        else:
            data = urllib2.urlopen(config.graphite_index_url).read()
        metrics = json.loads(data)
        metrics = filter(lambda x: x.startswith('servers.') and \
                    not is_bad_metric(x), metrics) # drop bad metrics
        if config.debug:
            open(config.metrics_file, 'w').write(json.dumps(metrics))
    except Exception, e:
        logging.warning(str(e))
        sys.exit(1)

def build_diamond():
    global metrics, diamond
    for metric in metrics:
        matched = filter(lambda x: x is not None, \
            map(lambda x: x.match(metric), [diamond_re_more, diamond_re]))
        if matched:
            match = matched[0].groupdict()
        else:
            continue
        server = match.get('server')
        plugin = match.get('plugin')
        if match.has_key('more'):
            plugin = plugin + '-' + match.get('more')
        if not diamond[server].has_key(plugin):
            diamond[server][plugin] = []
        diamond[server][plugin].append(metric)

logging.info('build metrics...')
build_metrics()

logging.info('build diamond...')
build_diamond()


def search_metrics(search):
    global metrics
    matched_metrics = []
    try:
        re_obj = re.compile(search, re.IGNORECASE)
    except:
        return None
    for m in metrics:
        if re_obj.search(m):
            matched_metrics.append(m)
    return matched_metrics

def do_groupby(search, index):
    matched_metrics = search_metrics(search)
    return [(g[0], list(g[1])) for g in itertools.groupby(sorted(matched_metrics, \
            key = lambda x:x.split('.')[int(index)]), \
            lambda x:x.split('.')[int(index)])]

def do_plugin(plugin, server_regex):
    global diamond
    data = {}
    re_obj = re.compile(server_regex)
    for s in diamond.keys():
        if re_obj.match(s):
            if diamond[s].has_key(plugin):
                data[s] = diamond[s][plugin]
    return data

def get_plugin_paths():
    global metrics
    data = defaultdict(dict) # dict is faster than set
    for m in metrics:
        o = diamond_re.match(m)
        if o:
            d = o.groupdict()
            server = d.get('server')
            plugin = d.get('plugin')
            path = m[len('servers.%s.%s.' % (server, plugin)):]
            data[plugin][path] = True
    return data



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
    for s in diamond.keys():
        prefix  = re.sub('\d+$', '', s)
        for p in diamond[s].keys():
            plugins[p][prefix] = True # dict is faster than set
    body = template('templates/dashboard', **locals())
    return render_page(body, page = 'dashboard')

@route('/server/<server>', method = 'GET')
def server(server = ''):
    global diamond
    graphs = []
    for plugin in sorted(diamond[server].keys()):
        graphs.append(Graph(diamond[server][plugin], title = server + ' ' + plugin))
    body = template('templates/plugin-multi', **locals())
    return render_page(body)

@route('/server/<server>/<plugin>', method = 'GET')
def plugin(server = '', plugin = ''):
    global diamond
    graph = Graph(diamond[server][plugin], title = server + ' ' + plugin)
    graph.graph_args['height'] = 400
    graph.tune_height(plugin)
    body = template('templates/plugin', **locals())
    return render_page(body)

@route('/metric/<metric_name>', method = 'GET')
def metric(metric_name = ''):
    targets = metric_name.split(',')
    title = request.query.get('title', metric_name)
    graph = Graph(targets, title = title)
    body = template('templates/metric', **locals())
    return render_page(body)

@route('/metrics/<metric_name>', method = 'GET')
def _metrics(*args, **kwargs):
    return metric(*args, **kwargs)

@route('/regex/', method = 'GET')
@route('/regex/', method = 'POST')
def regex():
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
        elif ':' in search:
            if search.startswith('plugin:'): # search == 'plugin:<plugin>:<server_regex>'
                _, plugin, server_regex = search.strip().split(':', 2)
                graphs = []
                data = do_plugin(plugin, server_regex)
                for server in sorted(data.keys()):
                    graph = Graph(data[server], title = server + ' ' + plugin)
                    graph.tune_height(plugin)
                    graphs.append(graph)
                body = template('templates/plugin-multi', **locals())
            elif search.startswith('merge:'): # search == 'merge:'
                _, regex = search.strip().split(':', 1)
                graph = Graph(targets =  search_metrics(regex), title = 'a merged graph')
                body = template('templates/merge', **locals())
        else: # search is common regex without any prefix
            match = groupby_re.match(search)
            if match:
                graphs = [ Graph(targets, title = group) for group, targets \
                    in do_groupby(**match.groupdict()) ]
                body = template('templates/groupby', **locals())
            else:
                data = search_metrics(search)
                if len(data) == 0:
                    errors.append('no metric is matched')
                graphs = [ Graph(targets = [metric, ], title = metric) for metric in data ]
                body = template('templates/list', **locals())
    if errors:
        body = template('templates/error', **locals())
    return render_page(body, search = search)

@route('/debug', method = 'GET')
def debug():
    global diamond, metrics
    data = get_plugin_paths()
    body = template('templates/debug', data = data, diamond = diamond, metrics = metrics)
    return render_page(body, page = 'debug')

@route('/docs', method = 'GET')
def docs():
    body = template('templates/docs')
    return render_page(body, page = 'docs')

@route('<path:re:/favicon.ico>', method = 'GET')
@route('<path:re:/static/css/.*css>', method = 'GET')
@route('<path:re:/static/js/.*js>', method = 'GET')
@route('<path:re:/static/fonts/.*woff>', method = 'GET')
def static(path):
    return static_file(path, root = '.')


