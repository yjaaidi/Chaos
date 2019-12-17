# Copyright (c) since 2001, Kisio Digital and/or its affiliates. All rights reserved.

VERSION = 'v1.2.24'

# http://bugs.python.org/issue7980
import datetime
datetime.datetime.strptime('', '')

# replace blocking method by a non blocking equivalent
# this enable us to use gevent for launching background task
from gevent import monkey
monkey.patch_all(thread=False, subprocess=False, os=False, signal=False)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging.config
import sys
from chaos.utils import Request
from chaos.publisher import Publisher
from flask_cache import Cache

app = Flask(__name__)
app.config.from_object('chaos.default_settings')
app.config.from_envvar('CHAOS_CONFIG_FILE')
app.request_class = Request


if 'LOGGER' in app.config:
    logging.config.dictConfig(app.config['LOGGER'])
else:  # Default is std out
    handler = logging.StreamHandler(stream=sys.stdout)
    app.logger.addHandler(handler)
    app.logger.setLevel('INFO')


db = SQLAlchemy(app)

publisher = Publisher(app.config['RABBITMQ_CONNECTION_STRING'], app.config['EXCHANGE'], app.config['ENABLE_RABBITMQ'])
cache = Cache(app, config=app.config['CACHE_CONFIGURATION'])

import chaos.api
