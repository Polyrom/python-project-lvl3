import os
import shutil
import sys
import requests
import logging
from .html_formatter import format_html
from .filename_formatter import get_basic_filename
from .assets_loader import download_assets

console_logger = logging.getLogger("console_log.page_loader")


def download(url, output):  # noqa: C901

    if not os.path.exists(output):
        raise FileNotFoundError

    console_logger.info("Making request to server")
    try:
        rs = requests.get(url)
        rs.raise_for_status()
    except (
            requests.exceptions.HTTPError,
            requests.exceptions.RequestException
    ):
        raise

    original_html = rs.text
    basic_filename = get_basic_filename(url)
    path_to_html = os.path.join(output, basic_filename + ".html")
    path_to_assets_dir = os.path.join(output, basic_filename + "_files")

    html, _ = format_html(
        url=url,
        text=original_html,
        directory=path_to_assets_dir
    )

    console_logger.info("Saving HTML file")
    try:
        save_html(html, path_to_html)
    except PermissionError:
        raise

    console_logger.info("Creating directory for page assets")
    try:
        create_assets_dir(path_to_assets_dir)
    except PermissionError:
        raise

    console_logger.info("Starting assets downloading")
    try:
        download_assets(
            url=url,
            text=original_html,
            directory=path_to_assets_dir
        )
    except (
        requests.exceptions.HTTPError,
        requests.exceptions.RequestException
    ):
        raise

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


def create_assets_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        console_logger.info("Removing old assets directory")
        shutil.rmtree(path)
        console_logger.info("Creating new assets directory")
        os.mkdir(path)
    except PermissionError:
        raise
