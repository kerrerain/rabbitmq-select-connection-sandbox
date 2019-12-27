import pika
import logging
import threading
import time

logger = logging.getLogger(__name__)


class Manager(threading.Thread):
    def __init__(self, consumers: list):
        threading.Thread.__init__(self)
        self._connection = None
        self._should_reconnect = False
        self._consumers = consumers

    def run(self):
        while True:
            try:
                self.start_connection_and_io_loop()
            except KeyboardInterrupt:
                break
            if self._should_reconnect:
                self.reconnect()

    def reconnect(self):
        logger.info("Reconnecting in 5s...")
        time.sleep(5)
        self._should_reconnect = False

    def start_connection_and_io_loop(self):
        self._connection = self.open_connection()
        self._connection.ioloop.start()

    def on_connected(self, connection):
        logger.info("Connected to broker")
        for consumer in self._consumers:
            connection.channel(on_open_callback=consumer.on_channel_open)

    def on_connection_open_error(self, connection, exception):
        if isinstance(exception, pika.exceptions.ConnectionClosedByClient) and exception.reply_code == 200:
            logger.info("Connection closed by client", exc_info=exception)
        else:
            logger.error("Connection lost", exc_info=exception)
            self._connection.ioloop.stop()
            self._should_reconnect = True

    def on_connection_close(self, connection, exception):
        self.on_connection_open_error(connection, exception)

    def open_connection(self) -> pika.SelectConnection:
        parameters = pika.ConnectionParameters()

        return pika.SelectConnection(
            parameters,
            on_open_callback=self.on_connected,
            on_open_error_callback=self.on_connection_open_error,
            on_close_callback=self.on_connection_close)
