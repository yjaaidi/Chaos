import os
import json
# URI for postgresql
# postgresql://<user>:<password>@<host>:<port>/<dbname>
# http://docs.sqlalchemy.org/en/rel_0_9/dialects/postgresql.html#psycopg2
SQLALCHEMY_DATABASE_URI = str(os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://navitia:navitia@localhost/chaos'))

DEBUG = (os.getenv('DEBUG', 1) == 1)

NAVITIA_URL = str(os.getenv('NAVITIA_URL', 'http://navitia2-ws.ctp.dev.canaltp.fr'))

# rabbitmq connections string: http://kombu.readthedocs.org/en/latest/userguide/connections.html#urls
RABBITMQ_CONNECTION_STRING = str(os.getenv('RABBITMQ_CONNECTION_STRING', 'pyamqp://guest:guest@localhost:5672//?heartbeat=60'))
#Cache configuration, see https://pythonhosted.org/Flask-Cache/ for more information
CACHE_CONFIGURATION = {
    'CACHE_TYPE': 'null',
    'TIMEOUT_PTOBJECTS': 600,
}

# amqp exhange used for sending disruptions
EXCHANGE = str(os.getenv('RABBITMQ_EXCHANGE', 'navitia'))

ENABLE_RABBITMQ = (os.getenv('RABBITMQ_ENABLED', 1) == 1)

ACTIVATE_PROFILING = (os.getenv('PROFILING_ENABLED', 0) == 1)

# Log Level available
# - DEBUG
# - INFO
# - WARN
# - ERROR

# logger configuration

from chaos.logging_utils import ChaosFilter

LOGGER = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(request_id)s] [%(levelname)5s] [%(process)5s] [%(name)25s] %(message)s',
        },
    },
    'filters': {
        'ChaosFilter': {
            '()': ChaosFilter,
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['ChaosFilter'],
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
        },
        'sqlalchemy.engine': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
        'sqlalchemy.pool': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
        'sqlalchemy.dialects.postgresql': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
    }
}
