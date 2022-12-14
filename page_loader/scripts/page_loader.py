#!/usr/bin/env python3
import sys
import logging
from page_loader.cli import parse_args
from page_loader import download

logging.basicConfig(level=logging.INFO)


def main():
    print("Starting downloading...")
    args = parse_args()

    try:
        filename = download(url=args.url, output=args.output)

    except Exception as err:
        logging.error(f"OOPS! An error occurred. "
                      f"Technical details below: \n{err}")
        sys.exit(1)

    else:
        print("Downloaded successfully!\n"
              "Your page is saved here:\n", filename)


if __name__ == '__main__':
    main()
