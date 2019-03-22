import sys
#from sources.daemon import impactsExportor
from sources.config import Config
from sources.database import init_db
import argparse
import logging
from sqlalchemy.exc import OperationalError


def main():
    parser = argparse.ArgumentParser(description="impacts exportor is in charge for creating export file")
    parser.add_argument('CONFIG_PERSIST', type=str)
    config_file = ""
    try:
        args = parser.parse_args()
        config_file = args.CONFIG_PERSIST
    except argparse.ArgumentTypeError:
        print("Bad usage, learn how to use me with %s -h" % sys.argv[0])
        sys.exit(1)
    config_data = Config()
    config_data.load(config_file)
    try:
        init_db(config_data.database)
    except OperationalError as e:
        logging.getLogger('database').warn("error while connecting on database: {}".format(str(e)))
        exit(1)
    #daemon = impactsExportor(config_data)
    #daemon.run()

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except:
        logging.exception('')
        raise
