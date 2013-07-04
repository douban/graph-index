#!/usr/bin/env python

import os
from bottle import run, debug

app_dir = os.path.dirname(__file__)
if app_dir:
    os.chdir(app_dir)

debug(True)
run('app', host = '0.0.0.0', port = 8088)
