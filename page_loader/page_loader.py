import os
import requests
from .html_formatter import format_html
from .filename_formatter import get_basic_filename
from .assets_loader import download_assets


def download(url, output):
    original_html = requests.get(url).text

    # build paths to formatted html, assets_dir & images
    basic_filename = get_basic_filename(url)
    path_to_assets_dir = os.path.join(output, basic_filename + "_files")
    path_to_html = os.path.join(output, basic_filename + ".html")

    # get formatted html
    html, _ = format_html(
        url=url,
        text=original_html,
        directory=path_to_assets_dir
    )

    # save formatted html
    with open(path_to_html, "w") as handler:
        handler.write(html)

    # create assets_directory
    os.mkdir(path_to_assets_dir)

    # download images to assets_dir
    download_assets(url=url, text=original_html, directory=path_to_assets_dir)

    # return path to formatted html
    return path_to_html
