import os
import logging
from pathlib import Path
from page_loader.url import build_basic_filepath
from page_loader.assets_loader import download_assets, format_html


def download(url, output):

    if not os.path.exists(output):
        raise FileNotFoundError

    basic_filename = build_basic_filepath(url)
    no_ext_filename = str(Path(basic_filename).with_suffix(""))

    html, assets, assets_dir = format_html(
        url=url,
        parent_dir=output,
        filename=no_ext_filename
    )

    path_to_html = os.path.join(output, basic_filename)
    logging.info("Saving HTML file")
    with open(path_to_html, "w") as handler:
        handler.write(html)

    download_assets(assets)

    return path_to_html
