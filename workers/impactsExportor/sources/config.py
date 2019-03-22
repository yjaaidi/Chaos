import logging
import logging.config
import json
import sys


class Config(object):
    """
    class de configuration de impacts exportor
    """
    def __init__(self):
        self.rabbitmq = None
        self.database = None
        self.timezone = 'Europe/Paris'

    def load(self, config_file):
        """
        Initialize from a configuration file.
        If not valid raise an error.
        """
        with open(config_file) as json_file:
            config_data = json.load(json_file)

            if 'logger' in config_data:
                logging.config.dictConfig(config_data['logger'])
            else:  # Default is std out
                handler = logging.StreamHandler(stream=sys.stdout)
                logging.getLogger().addHandler(handler)
                logging.getLogger().setLevel('INFO')

            if 'rabbitmq' in config_data:
                self.rabbitmq = config_data['rabbitmq']
            else:
                raise ValueError("Config is not valid, rabbitmq is needed")

            if 'database' in config_data:
                self.database = config_data['database']
            else:
                raise ValueError("Config is not valid, database is needed")

            if 'timezone' in config_data:
                self.timezone = config_data['timezone']
