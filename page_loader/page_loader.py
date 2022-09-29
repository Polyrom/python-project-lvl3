import os
import logging
from pathlib import Path
from html_formatter import format_html
from url import build_basic_filepath
from assets_loader import download_assets


def download(url, output):

    if not os.path.exists(output):
        raise FileNotFoundError

    basic_filename = build_basic_filepath(url)
    no_ext_filename = str(Path(basic_filename).with_suffix(""))

    html, download_info = format_html(
        url=url,
        parent_dir=output,
        filename=no_ext_filename
    )

    path_to_html = os.path.join(output, basic_filename)
    logging.info("Saving HTML file")
    with open(path_to_html, "w") as handler:
        handler.write(html)

    download_assets(assets_info=download_info,
                    parent_dir=output,
                    filename=no_ext_filename)

    return path_to_html
