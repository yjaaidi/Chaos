#URI for postgresql
# postgresql://<user>:<password>@<host>:<port>/<dbname>
#http://docs.sqlalchemy.org/en/rel_0_9/dialects/postgresql.html#psycopg2
SQLALCHEMY_DATABASE_URI = 'postgresql://navitia:navitia@localhost/chaos'

DEBUG = True

NAVITIA_URL = 'http://navitia2-ws.ctp.dev.canaltp.fr'
NAVITIA_COVERAGE = 'centre'
NAVITIA_TOKEN = 'f8a9befb-6bd9-4620-b942-b6b69a07487d'

#Log Level available
# - DEBUG
# - INFO
# - WARN
# - ERROR

# logger configuration

from chaos.logging_utils import ChaosFilter

LOGGER = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters':{
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
        'celery':{
            'level': 'INFO',
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
