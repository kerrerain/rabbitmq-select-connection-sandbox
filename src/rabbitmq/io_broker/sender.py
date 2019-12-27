import logging

logger = logging.getLogger(__name__)


class Sender():
    def __init__(self, name):
        self.channel = None
        self.name = name

    def on_channel_open(self, channel):
        self.channel = channel

    def send_message_to_queue(self, queue_name: str, message: str):
        logger.info("Sending message to queue {}".format(queue_name))

        self.channel.basic_publish(exchange="",
                                   routing_key=queue_name,
                                   body=message)

        logger.info("Message sent to queue {}".format(queue_name))
