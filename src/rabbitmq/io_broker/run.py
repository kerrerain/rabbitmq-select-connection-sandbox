import logging
from .manager import Manager
from .consumer import Consumer
from .sender import Sender
import time

logger = logging.getLogger(__name__)


def run():
    # Thread A
    consumer_1 = Consumer("consumer_1")
    consumer_2 = Consumer("consumer_2")
    manager = Manager(consumers=[consumer_1, consumer_2])
    manager.start()

    # Thread B
    sender = Sender("sender")
    manager_sender = Manager(consumers=[sender])
    manager_sender.start()

    time.sleep(1)

    sender.send_message_to_queue("test", "Baouh")
    sender.send_message_to_queue("test", "Obaho")
