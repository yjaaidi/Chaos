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
        self._connections = set([self._connection])#set of connection for the heartbeat
        self._exchange = Exchange(exchange, durable=True, delivry_mode=2, type='topic')
        self._connection.connect()
        monitor_heartbeats(self._connections)

    def _get_producer(self):
        producer = producers[self._connection].acquire(block=True, timeout=2)
        self._connections.add(producer.connection)
        return producer

    def publish(self, item, contributor):
        if not self._is_active:
            return

        with self._get_producer() as producer:
            producer.publish(item, exchange=self._exchange, routing_key=contributor, declare=[self._exchange])

    def info(self):
        if not self._is_active:
            return {}
        with self._get_producer() as producer:
            res = producer.connection.info()
            if 'password' in res:
                del res['password']
            return res


def monitor_heartbeats(connections, rate=2):
    """
    launch the heartbeat of amqp, it's mostly for prevent the f@#$ firewall from droping the connection
    """
    supports_heartbeats = False
    interval = 10000
    for conn in connections:
        if conn.heartbeat and conn.supports_heartbeats:
            supports_heartbeats = True
            interval = min(conn.heartbeat / 2, interval)

    if not supports_heartbeats:
        logging.getLogger(__name__).info('heartbeat is not enabled')
        return

    logging.getLogger(__name__).info('start rabbitmq monitoring')
    def heartbeat_check():
        for conn in connections:
            if conn.connected:
                logging.getLogger(__name__).debug('heartbeat_check for %s', conn)
                try:
                    conn.heartbeat_check(rate=rate)
                except ConnectionForced:
                    #I don't know why, but pyamqp fail to detect the heartbeat
                    #So even if it fail we don't do anything
                    pass
        spawn_later(interval, heartbeat_check)

    spawn_later(interval, heartbeat_check)
