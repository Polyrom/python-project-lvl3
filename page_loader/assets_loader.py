import requests
from .html_formatter import format_html


def download_assets(url, text, directory):
    _, download_info = format_html(url, text, directory)

    for asset_info in download_info:
        asset_url, new_path = asset_info

        with open(new_path, "wb") as handler:
            asset_data = requests.get(asset_url).content
            handler.write(asset_data)
