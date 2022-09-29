import os
import requests
import logging
from .html_formatter import format_html
from .filename_builder import build_basic_filepath
from .assets_loader import download_assets


def download(url, output):

    if not os.path.exists(output):
        raise FileNotFoundError

    logging.info("Making request to server")
    rs = requests.get(url)
    rs.raise_for_status()

    original_html = rs.text
    basic_filename = build_basic_filepath(url)

    html, download_info = format_html(
        url=url,
        text=original_html,
        parent_dir=output,
        filename=basic_filename
    )

    path_to_html = os.path.join(output, basic_filename + ".html")
    logging.info("Saving HTML file")
    if not os.path.exists(path_to_html):
        with open(path_to_html, "w") as handler:
            handler.write(html)

    download_assets(assets_info=download_info,
                    parent_dir=output,
                    filename=basic_filename)

    return path_to_html
