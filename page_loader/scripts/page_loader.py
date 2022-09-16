#!/usr/bin/env python3
import sys
import requests
import logging
from page_loader.cli import parse_args
from page_loader import download
from page_loader.config_loggers import init_console_logger

init_console_logger("console_log")
console_logger = logging.getLogger("console_log.main")


def main():
    print("Starting downloading...")
    args = parse_args()

    try:
        filename = download(url=args.url, output=args.output)

    except requests.exceptions.HTTPError as http_err:
        console_logger.error(f"OOPS! "
                             f"An HTTP error occurred "
                             f"while making a request to server. "
                             f"Technical details below:\n"
                             f"{str(http_err)}")
        sys.exit(0)

    except requests.exceptions.RequestException as req_err:
        console_logger.error(f"OOPS! "
                             f"An error occurred "
                             f"while making a request to server. "
                             f"Technical details below:\n"
                             f"{str(req_err)}")
        sys.exit(0)

    except PermissionError:
        console_logger.error(f"Make sure "
                             f"you have access rights "
                             f"to write files in the following directory:"
                             f" {args.output}.")
        sys.exit(0)

    except FileNotFoundError:
        console_logger.error(f"Invalid path: "
                             f"{args.output}. Make sure "
                             f"the directory exists.")
        sys.exit(0)

    else:
        print("Downloaded successfully!\n"
              "Your page is saved here:\n", filename)


if __name__ == '__main__':
    main()
