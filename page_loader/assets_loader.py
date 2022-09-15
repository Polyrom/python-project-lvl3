import requests
import logging
import errno
from progress.bar import ShadyBar
from .html_formatter import format_html

file_logger = logging.getLogger("file_log.assets_loader")
console_logger = logging.getLogger("console_log.assets_loader")


def download_assets(url, text, directory):
    _, download_info = format_html(url, text, directory)
    progress_bar = ShadyBar("Downloading...",
                            max=len(download_info),
                            suffix="%(percent)d%% - Remaining time: %(eta)ds")
    for asset_info in progress_bar.iter(download_info):
        asset_url, new_path = asset_info
        try:
            with open(new_path, "wb") as handler:
                file_logger.info(f"Downloading asset {asset_url}")
                req = requests.get(asset_url)
                req.raise_for_status()
                asset_data = req.content
                handler.write(asset_data)
        except OSError as os_err:
            if os_err.errno == errno.ENAMETOOLONG:
                file_logger.info(f"Could not download asset from {asset_url} "
                                 f"due to too long name.")
                file_logger.info(f"Could not download asset from {asset_url} "
                                 f"due to too long name. Continuing...")
                continue
            else:
                raise
