import os
import sys
import requests
import logging
from .html_formatter import format_html
from .filename_formatter import get_basic_filename
from .assets_loader import download_assets

console_logger = logging.getLogger("console_log.page_loader")


def download(url, output):

    if not os.path.exists(output):
        raise FileNotFoundError

    console_logger.info("Making request to server")
    rs = requests.get(url)
    rs.raise_for_status()

    original_html = rs.text
    basic_filename = get_basic_filename(url)
    path_to_assets_dir = os.path.join(output, basic_filename + "_files")

    html, download_info = format_html(
        url=url,
        text=original_html,
        directory=path_to_assets_dir
    )

    path_to_html = os.path.join(output, basic_filename + ".html")
    console_logger.info("Saving HTML file")
    save_html(html, path_to_html)

    console_logger.info("Creating directory for page assets")
    if not os.path.exists(path_to_assets_dir):
        os.mkdir(path_to_assets_dir)

    console_logger.info("Starting assets downloading")
    download_assets(download_info)

    return path_to_html


def save_html(html, path):
    if os.path.exists(path):
        answer = input("This HTML file already exists. "
                       "Do you want to rewrite it? [yes/no]\n")
        if answer.lower() == "yes":
            console_logger.info("HTML will be rewritten.")
        elif answer.lower() == "no":
            console_logger.critical("Rewriting aborted. Bye!")
            sys.exit(0)
        else:
            console_logger.critical("Sorry, I didn't get you. "
                                    "Type either 'yes' or 'no'. "
                                    "Rewriting aborted. Bye!")
            sys.exit(0)
    try:
        with open(path, "w") as handler:
            handler.write(html)
    except PermissionError:
        raise
