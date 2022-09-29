import os
import requests
import logging
from progress.bar import ShadyBar


def download_assets(assets_info, parent_dir, filename):

    assets_dir = create_assets_dir_name(parent_dir, filename)
    logging.info("Creating directory for page assets")
    if not os.path.exists(assets_dir):
        os.mkdir(assets_dir)

    logging.info("Starting assets downloading")
    progress_bar = ShadyBar("Downloading...",
                            max=len(assets_info),
                            suffix="%(percent)d%% - Remaining time: %(eta)ds")
    for asset_info in progress_bar.iter(assets_info):
        asset_url, new_path = asset_info
        with open(new_path, "wb") as handler:
            req = requests.get(asset_url)
            req.raise_for_status()
            asset_data = req.content
            handler.write(asset_data)


def create_assets_dir_name(directory, filename):
    return os.path.join(directory, filename + "_files")
