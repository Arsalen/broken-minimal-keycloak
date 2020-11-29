#!/usr/bin/env python3

import os

try:
    bind = os.environ["WEB_BIND"]
    workers = os.environ["WEB_WORKERS"]
    loglevel = os.environ["WEB_LOG_LEVEL"]
    reload = os.environ["WEB_RELOAD"]
except Exception as ex:
    raise