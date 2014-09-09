from kombu import BrokerConnection, Exchange
from kombu.pools import producers, connections

class Publisher(object):
    def __init__(self, connection_string, exchange, is_active=True):
        self._is_active = is_active
        if not is_active:
            return

        self._connection = BrokerConnection(connection_string)
        self._exchange = Exchange(exchange, durable=True, delivry_mode=2, type='topic')

    def publish(self, item, contributor):
        if not self._is_active:
            return

        with connections[self._connection].acquire(block=True, timeout=2) as connection:
            with producers[connection].acquire(block=True, timeout=2) as producer:
                producer.publish(item, exchange=self._exchange, routing_key=contributor, declare=[self._exchange])

    def info(self):
        if not self._is_active:
            return {}
        with connections[self._connection].acquire(block=True, timeout=2) as connection:
            res = connection.info()
            if 'password' in res:
                del res['password']
            return res
