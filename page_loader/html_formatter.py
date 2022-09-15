import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from .filename_formatter import get_basic_filename


def format_html(url, text, directory):

    html = BeautifulSoup(text, "html.parser")
    image_tags = html.find_all("img", src=True)
    link_tags = html.findAll("link", href=True)
    script_tags = html.findAll("script", src=True)
    tags = image_tags + link_tags + script_tags
    download_data = []

    for tag in tags:
        asset_link = get_link(tag)
        _, extension = os.path.splitext(asset_link)

        if is_same_domain(url, asset_link):
            asset_url = urljoin(url, asset_link)
            asset_name = get_basic_filename(asset_url) + extension
            new_path = os.path.join(directory, asset_name)

            if tag.has_attr("href"):
                asset_info = asset_url, new_path
                download_data.append(asset_info)
                tag["href"] = new_path
            elif tag.has_attr("src"):
                asset_info = asset_url, new_path
                download_data.append(asset_info)
                tag["src"] = new_path

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


def get_link(tag):
    if tag.has_attr("href"):
        return tag["href"]
    elif tag.has_attr("src"):
        return tag["src"]
