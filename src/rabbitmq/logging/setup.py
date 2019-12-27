import os
from pathlib import Path
import json
import logging.config


def setup_logging():
    path = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'logging.json')

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)

        log_output_path = _create_log_output_path(".makesense_log")
        config["handlers"]["file"]["filename"] = log_output_path

        logging.config.dictConfig(config)
        logger = logging.getLogger("rabbitmq")
        logger.info(
            "Initialization of the logger done - log output file in {}".format(log_output_path))
    else:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("rabbitmq")
        logger.warning("Initialization of the logger using basic config")


def _create_log_output_path(default_log_dir):
    log_output_dir = os.path.join(str(Path.home()), default_log_dir)

    if not os.path.exists(log_output_dir):
        os.mkdir(log_output_dir)

    return os.path.join(log_output_dir, "rabbitmq.log")
