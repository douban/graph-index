#!/usr/bin/env python

import os
import re
import sys
import json
import pickle
import urllib2
import logging
import itertools
from collections import defaultdict

import config

logging.basicConfig(format = '%(asctime)-15s %(message)s', level = logging.DEBUG)

bad_metrics = [
    re.compile('^servers\.[^\.]+\.memory\.Vmalloc.*$'),
    re.compile('^servers\.[^\.]+\.processresources\.[^\.]+\.vms$'),
    re.compile('^servers\.[^\.]+\.cpu\.total\.idle$'),
]

diamond_re = re.compile('^servers\.(?P<server>[^\.]+)\.(?P<plugin>[^\.]+)\..*$')
diamond_re_more = re.compile('^servers\.(?P<server>[^\.]+)\.(?P<plugin>(network|iostat))\.(?P<more>[^\.]+)\..*$')
groupby_re = re.compile('^(?P<search>[^ ]*)\s+group\s*by\s*(?P<index>\-?\d+)$')

def is_bad_metric(metric):
    for r in bad_metrics:
        if r.match(metric):
            return True

def build_metrics():
    try:
        oldmetrics = []
        if os.path.exists(config.metrics_file):
            oldmetrics = json.loads(open(config.metrics_file).read())
            if config.debug:
                return oldmetrics
        newmetrics = json.loads(urllib2.urlopen(config.graphite_index_url).read())
        newmetrics = filter(lambda x: not is_bad_metric(x), newmetrics) # drop bad metrics
        newmetrics.sort()
        oldmetrics.sort()
        if newmetrics != oldmetrics:
            open(config.metrics_file, 'w').write(json.dumps(newmetrics))
        return newmetrics
    except Exception as e:
        logging.warning(str(e))
        sys.exit(1)

def build_diamond(metrics):
    diamond = defaultdict(dict)
    for metric in metrics:
        matched = filter(lambda x: x is not None, \
            map(lambda x: x.match(metric), [diamond_re_more, diamond_re]))
        if matched:
            match = matched[0].groupdict()
        else:
            continue
        server = match.get('server')
        plugin = match.get('plugin')
        if 'more' in match:
            plugin = plugin + '.' + match.get('more')
        if plugin not in diamond[server]:
            diamond[server][plugin] = []
        diamond[server][plugin].append(metric)
    open(config.diamond_cache, 'wb').write(pickle.dumps(diamond))
    return diamond

def search_metrics(metrics, search):
    matched_metrics = []
    try:
        re_obj = re.compile(search, re.IGNORECASE)
    except:
        return None
    for m in metrics:
        if re_obj.search(m):
            matched_metrics.append(m)
    return matched_metrics

def do_groupby(metrics, search = None, index = None):
    matched_metrics = search_metrics(metrics, search)
    return [(g[0], list(g[1])) for g in itertools.groupby(sorted(matched_metrics, \
            key = lambda x:x.split('.')[int(index)]), \
            lambda x:x.split('.')[int(index)])]

def do_plugin(diamond, plugin, server_regex):
    data = {}
    re_obj = re.compile(server_regex)
    for s in diamond.keys():
        if re_obj.match(s):
            if plugin in diamond[s]:
                data[s] = diamond[s][plugin]
    return data
