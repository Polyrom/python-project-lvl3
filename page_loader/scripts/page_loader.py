#!/usr/bin/env python3
import logging
from page_loader.cli import parse_args
from page_loader import download


def init_logger(name):
    logger = logging.getLogger(name)
    FORMAT = "%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s"
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.debug("Logger was initialized")


init_logger("app")
logger = logging.getLogger("app.main")


def main():
    args = parse_args()
    filename = download(args.url, args.output)
    print("Your page is saved here:\n", filename)


if __name__ == '__main__':
    main()
