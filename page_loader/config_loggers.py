import logging
import logging.handlers


def init_file_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    FORMAT = "%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s"
    fh = logging.handlers.RotatingFileHandler(
        filename="logs/logs.log",
        maxBytes=1000000
    )
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.debug("Logger was initialized")


def init_console_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    FORMAT = "%(message)s"
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.INFO)
    logger.addHandler(sh)
