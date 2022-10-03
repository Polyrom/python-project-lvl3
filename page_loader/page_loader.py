import os
import logging
from page_loader.url import build_basic_filepath
from page_loader.assets_loader import download_assets, prepare_data


def download(url, output):

    if not os.path.exists(output):
        raise FileNotFoundError

    html, assets = prepare_data(
        url=url,
        parent_dir=output
    )

    path_to_html = os.path.join(output, build_basic_filepath(url))
    logging.info("Saving HTML file")
    with open(path_to_html, "w") as handler:
        handler.write(html)

    download_assets(assets)

    return path_to_html
