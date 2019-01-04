from nameko.events import event_handler
from nameko.messaging import Publisher
from kombu.messaging import Exchange


class WorkerSubscriber:
    name = 'worker_subscriber'

    test = Exchange('test', type='direct')
    publish = Publisher(exchange=test)

    @event_handler("api", "say_hello")
    def handle_event(self, payload):
        print("{0} said hello!".format(payload))
        self.publish("Goodbye {0}".format(payload))

