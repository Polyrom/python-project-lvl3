import os
import requests
import logging
from bs4 import BeautifulSoup
from progress.bar import ShadyBar
from urllib.parse import urljoin
from page_loader.url import is_same_domain, make_asset_name


def download_assets(assets_info):

    logging.info("Starting assets downloading")
    progress_bar = ShadyBar("Downloading...",
                            max=len(assets_info),
                            suffix="%(percent)d%% - Remaining time: %(eta)ds")
    for asset_info in progress_bar.iter(assets_info):
        asset_url, new_path = asset_info
        with open(new_path, "wb") as handler:
            req = requests.get(asset_url)
            req.raise_for_status()
            handler.write(req.content)


def generate_assets_dir_name(directory, filename):
    no_ext_filename, _ = os.path.splitext(filename)
    return os.path.join(directory, no_ext_filename + "_files")


def format_html(url, parent_dir, filename):
    logging.info("Making request to server")
    rs = requests.get(url)
    rs.raise_for_status()

    html = BeautifulSoup(rs.text, "html.parser")
    image_tags = html.find_all("img", src=True)
    link_tags = html.findAll("link", href=True)
    script_tags = html.findAll("script", src=True)
    tags = image_tags + link_tags + script_tags

    assets_dir = generate_assets_dir_name(parent_dir, filename)
    logging.info("Creating directory for page assets")
    if not os.path.exists(assets_dir):
        os.mkdir(assets_dir)
    assets = []

    for tag in tags:
        attr = "href" if tag.has_attr("href") else "src"
        asset_link = tag[attr]

        if is_same_domain(url, asset_link):
            asset_url = urljoin(url, asset_link)
            asset_name = make_asset_name(url, asset_link)
            abs_path = os.path.join(assets_dir, asset_name)
            rel_path = os.path.join(assets_dir.rsplit("/")[-1], asset_name)
            asset_info = asset_url, abs_path
            assets.append(asset_info)
            tag[attr] = rel_path

    return html.prettify(), assets, assets_dir
