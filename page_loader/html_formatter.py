import os
import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from page_loader.url import build_basic_filepath
from page_loader.assets_loader import create_assets_dir_name


def format_html(url, parent_dir, filename):
    logging.info("Making request to server")
    rs = requests.get(url)
    rs.raise_for_status()
    html = BeautifulSoup(rs.text, "html.parser")
    image_tags = html.find_all("img", src=True)
    link_tags = html.findAll("link", href=True)
    script_tags = html.findAll("script", src=True)
    tags = image_tags + link_tags + script_tags
    assets_dir = create_assets_dir_name(parent_dir, filename)
    download_data = []

    for tag in tags:
        attr = "href" if tag.has_attr("href") else "src"
        asset_link = tag[attr]

        if is_same_domain(url, asset_link):
            asset_url = urljoin(url, asset_link)
            asset_name = make_asset_name(url, asset_link)
            abs_path = os.path.join(assets_dir, asset_name)
            rel_path = os.path.join(assets_dir.rsplit("/")[-1], asset_name)
            asset_info = asset_url, abs_path
            download_data.append(asset_info)
            tag[attr] = rel_path

    return html.prettify(), download_data


def is_same_domain(html_url, asset_url):
    parsed_asset_url = urlparse(asset_url)
    parsed_html_url = urlparse(html_url)
    asset_netloc = parsed_asset_url.netloc.strip("www.")
    html_netloc = parsed_html_url.netloc.strip("www.")
    _, extension = os.path.splitext(asset_url)
    if asset_netloc == html_netloc or asset_netloc == "":
        return True
    return False


def make_asset_name(url, link):
    link_path, ext = os.path.splitext(link)
    asset_url_no_ext = urljoin(url, link_path)
    filename, _ = os.path.splitext(build_basic_filepath(asset_url_no_ext))
    asset_extension = ".html" if ext == "" else ext
    return filename + asset_extension
