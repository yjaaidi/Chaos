from kombu import BrokerConnection, Exchange
from kombu.pools import producers, connections
import logging
from amqp.exceptions import ConnectionForced

from gevent import spawn_later
import weakref

class Publisher(object):
    def __init__(self, connection_string, exchange, contributor, is_active=True):
        self._is_active = is_active
        self._contributor = contributor
        if not is_active:
            return

        self._connection = BrokerConnection(connection_string)
        self._exchange = Exchange(exchange, durable=True, delivry_mode=2, type='topic')
        self._connection.connect()
        monitor_heartbeats(self._connection)

    def publish(self, item, contributor):
        if not self._is_active:
            return

        with producers[self._connection].acquire(block=True, timeout=2) as producer:
            producer.publish(item, exchange=self._exchange, routing_key=contributor, declare=[self._exchange])

    def info(self):
        if not self._is_active:
            return {}
        with connections[self._connection].acquire(block=True, timeout=2) as connection:
            res = connection.info()
            if 'password' in res:
                del res['password']
            return res


def monitor_heartbeats(connection, rate=2):
    """
    launch the heartbeat of amqp, it's mostly for prevent the f@#$ firewall from droping the connection
    """
    if not connection.heartbeat or not connection.supports_heartbeats:
        logging.getLogger(__name__).warn('amqp heartbeat is not enable!')
        return
    logging.getLogger(__name__).info('start rabbitmq monitoring')
    interval = connection.heartbeat / 2
    cref = weakref.ref(connection)

    def heartbeat_check():
        conn = cref()
        if conn and conn.connected:
            logging.getLogger(__name__).debug('heartbeat_check')
            try:
                conn.heartbeat_check(rate=rate)
            except ConnectionForced:
                #I don't know why, but pyamqp fail to detect the heartbeat
                #So even if it fail we don't do anything
                pass
            spawn_later(interval, heartbeat_check)
        else:
            logging.getLogger(__name__).info('monitoring rabbitmq stopped')

    spawn_later(interval, heartbeat_check)
