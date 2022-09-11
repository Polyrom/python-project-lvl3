import os
import sys
import requests
import logging
from .html_formatter import format_html
from .filename_formatter import get_basic_filename
from .assets_loader import download_assets

logger = logging.getLogger("app.page_loader")


def download(url, output):
    logger.info("Starting downloading...")
    try:
        logger.info("Making request to server...")
        original_html = requests.get(url).text
    except ConnectionError as err:
        logger.error(err)
        print(f"Could not connect to server. Error: {str(err)}")
        sys.exit()
    logger.info("Server responded successfully")

    basic_filename = get_basic_filename(url)
    path_to_assets_dir = os.path.join(output, basic_filename + "_files")
    path_to_html = os.path.join(output, basic_filename + ".html")

    html, _ = format_html(
        url=url,
        text=original_html,
        directory=path_to_assets_dir
    )
    logger.info("Saving HTML file...")

    try:
        with open(path_to_html, "w") as handler:
            handler.write(html)
    except IOError as err:
        logger.error(err)
        print(f"Could not save the HTML. Error: {str(err)}")
        sys.exit()
    else:
        logger.info("HTML file saved successfully!")

    logger.info("Creating directory for page assets...")

    try:
        os.mkdir(path_to_assets_dir)
    except IOError as err:
        logger.error(err)
        print(f"Could not create assets directory! Error: {str(err)}")
        sys.exit()
    logger.info("Directory created successfully!")

    logger.info("Starting assets downloading...")
    download_assets(url=url, text=original_html, directory=path_to_assets_dir)
    logger.info("Assets downloaded successfully!")
    logger.info("Download finished!")
    return path_to_html
