#!/usr/bin/env python3
import sys
import requests
import logging
import logging.handlers
from colorama import init, Fore, Style
from page_loader.cli import parse_args
from page_loader import download

# initializing colorama for nice output
init()


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


init_file_logger("file_log")
file_logger = logging.getLogger("file_log.main")


init_console_logger("console_log")
console_logger = logging.getLogger("console_log.main")


def main():
    print(Fore.GREEN + Style.BRIGHT + "Starting downloading...")
    args = parse_args()

    try:
        filename = download(args.url, args.output)

    except requests.exceptions.HTTPError as http_err:
        file_logger.error(f"HTTP Error occurred: {str(http_err)}")
        console_logger.error(Fore.RED + Style.BRIGHT + f"OOPS! "
                             f"An HTTP error occurred "
                             f"while making a request to server. "
                             f"Technical details below:\n"
                             f"{str(http_err)}")
        print(Fore.RESET + Style.RESET_ALL)
        sys.exit(1)

    except requests.exceptions.RequestException as req_err:
        file_logger.critical(f"Request Error occurred: {str(req_err)}")
        console_logger.error(Fore.RED + Style.BRIGHT + f"OOPS! "
                             f"An error occurred "
                             f"while making a request to server. "
                             f"Technical details below:\n"
                             f"{str(req_err)}")
        print(Fore.RESET + Style.RESET_ALL)
        sys.exit(1)

    except PermissionError as perm_err:
        file_logger.critical(f"Permission Error occurred: {perm_err}")
        console_logger.error(Fore.RED + Style.BRIGHT + f"Make sure "
                             f"you have access rights "
                             f"to write files in the following directory:"
                             f" {args.output}.")
        print(Fore.RESET + Style.RESET_ALL)
        sys.exit(1)

    except FileNotFoundError as not_found_err:
        file_logger.critical(f"Invalid path: {not_found_err}")
        console_logger.error(Fore.RED + Style.BRIGHT + f"Invalid path: "
                             f"{args.output}. Make sure "
                             f"the directory exists.")
        print(Fore.RESET + Style.RESET_ALL)
        sys.exit(1)

    else:
        print("Downloaded successfully!\n"
              "Your page is saved here:\n", filename)


if __name__ == '__main__':
    main()
