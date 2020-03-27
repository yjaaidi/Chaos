import os
# URI for postgresql
# postgresql://<user>:<password>@<host>:<port>/<dbname>
# http://docs.sqlalchemy.org/en/rel_0_9/dialects/postgresql.html#psycopg2
SQLALCHEMY_DATABASE_URI = str(os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://navitia:navitia@localhost/chaos_cust'))

DEBUG = True

NAVITIA_URL = 'http://navitia2-ws.ctp.customer.canaltp.fr'
NAVITIA_TIMEOUT = 5

# rabbitmq connections string: http://kombu.readthedocs.org/en/latest/userguide/connections.html#urls
RABBITMQ_CONNECTION_STRING = 'pyamqp://guest:guest@localhost:5672//?heartbeat=60'

# Cache configuration, see https://pythonhosted.org/Flask-Cache/ for more information
cache_type = 'redis'

CACHE_CONFIGURATION = {
    'CACHE_TYPE': cache_type,
    'CACHE_DEFAULT_TIMEOUT': 86400,  # in seconds
    'NAVITIA_CACHE_TIMEOUT': 2 * 24 * 3600,  # in seconds
    'NAVITIA_PUBDATE_CACHE_TIMEOUT': 600,  # in seconds
}

if cache_type == 'redis':
    CACHE_CONFIGURATION['CACHE_REDIS_HOST'] = '127.0.0.1'
    CACHE_CONFIGURATION['CACHE_REDIS_PORT'] = 6379
    CACHE_CONFIGURATION['CACHE_REDIS_PASSWORD'] = None
    CACHE_CONFIGURATION['CACHE_REDIS_DB'] = 0
    CACHE_CONFIGURATION['CACHE_KEY_PREFIX'] = 'Chaos'

# amqp exchange used for sending disruptions
EXCHANGE = 'navitia'

ENABLE_RABBITMQ = False

ACTIVATE_PROFILING = False

SQLALCHEMY_ECHO = True

# Directory for store export files
IMPACT_EXPORT_DIR = '/tmp'
# Path of python if problem with venv
IMPACT_EXPORT_PYTHON = ''

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

# Newrelic file
NEW_RELIC_CONFIG_FILE = str(os.getenv('NEW_RELIC_CONFIG_FILE', None))
