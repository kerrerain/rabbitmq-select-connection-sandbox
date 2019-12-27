import logging
import pika
from rabbitmq.logging.setup import setup_logging
from rabbitmq.io_broker.run import run

logger = logging.getLogger("rabbitmq")

if __name__ == "__main__":
    setup_logging()
    run()
