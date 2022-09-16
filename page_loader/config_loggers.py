import logging


def init_console_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    FORMAT = "%(asctime)s - %(message)s"
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.INFO)
    logger.addHandler(sh)
