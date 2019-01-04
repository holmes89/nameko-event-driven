from nameko.messaging import consume
from kombu.messaging import Exchange, Queue


class Consumer:
    name = 'worker_consumer'
    test = Exchange('test', type='direct')
    tq = Queue('q1', exchange=test)

    @consume(tq)
    def handle_consume(self, body):
        print("Received message: {0}".format(body))
