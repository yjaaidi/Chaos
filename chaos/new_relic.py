import logging
import flask
import os

try:
    from newrelic import agent
except ImportError:
    logger = logging.getLogger(__name__)
    logger.warn('New Relic is not available')
    agent = None


def init(config):
    if not agent or not config:
        return
    if os.path.exists(config):
        agent.initialize(config)
    else:
        logging.getLogger(__name__).error('%s doesn\'t exist, newrelic disabled', config)


def record_exception():
    """
    record the exception currently handled to newrelic
    """
    if agent:
        agent.record_exception()  # will record the exception currently handled


def record_custom_parameter(name, value):
    """
    add a custom parameter to the current request
    """
    if agent:
        agent.add_custom_parameter(name, value)
