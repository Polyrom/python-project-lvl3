import requests
import logging
import errno
from progress.bar import ShadyBar

console_logger = logging.getLogger("console_log.assets_loader")


def download_assets(assets_info):
    progress_bar = ShadyBar("Downloading...",
                            max=len(assets_info),
                            suffix="%(percent)d%% - Remaining time: %(eta)ds")
    for asset_info in progress_bar.iter(assets_info):
        asset_url, new_path = asset_info
        try:
            with open(new_path, "wb") as handler:
                req = requests.get(asset_url)
                req.raise_for_status()
                asset_data = req.content
                handler.write(asset_data)
        except OSError as os_err:
            if os_err.errno == errno.ENAMETOOLONG:
                console_logger.info(f"Could not download asset from "
                                    f"{asset_url} due to "
                                    f"too long name.")
                continue
            else:
                raise
