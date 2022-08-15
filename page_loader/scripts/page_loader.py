#!/usr/bin/env python3
from page_loader.cli import parse_args
from page_loader import download


def main():
    args = parse_args()
    filename = download(args.url, args.output)
    print(filename)


if __name__ == '__main__':
    main()
