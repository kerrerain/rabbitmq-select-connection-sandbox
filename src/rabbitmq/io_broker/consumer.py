import logging
import functools

logger = logging.getLogger(__name__)


class Consumer():
    def __init__(self, name):
        self.channel = None
        self.name = name

    def on_channel_open(self, channel):
        self.channel = channel
        channel.queue_declare(queue="test", durable=True, exclusive=False,
                              auto_delete=False, callback=self.on_queue_declared)

    def on_queue_declared(self, frame):
        self.channel.basic_consume("test", self.handle_delivery)
        logger.info("(consumer={}) Waiting for messages".format(self.name))

    def handle_delivery(self, channel, method, header, body):
        logger.info("(consumer={}) Message: {}".format(self.name, body))
        channel.basic_ack(method.delivery_tag)
