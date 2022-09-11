import sys
import requests
import logging
from .html_formatter import format_html

logger = logging.getLogger("app.assets_loader")


def download_assets(url, text, directory):
    _, download_info = format_html(url, text, directory)
    for asset_info in download_info:
        asset_url, new_path = asset_info

        try:
            with open(new_path, "wb") as handler:
                asset_data = requests.get(asset_url).content
                handler.write(asset_data)
                logger.info(f"Asset saved at {new_path}")
        except ConnectionError as con_err:
            logger.error(con_err)
            print(f"Could not download page assets! Error: {str(con_err)}")
            sys.exit()
        except IOError as io_err:
            logger.error(io_err)
            print(f"Could not save the page assets! Error: {str(io_err)}")
            sys.exit()
