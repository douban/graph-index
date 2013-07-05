#!/usr/bin/env python

import os
from bottle import run, debug

import config

app_dir = os.path.dirname(__file__)
if app_dir:
    os.chdir(app_dir)

debug(True)

run('app', host = config.listen_host, port = config.listen_port, reloader = True)
