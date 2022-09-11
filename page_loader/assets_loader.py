import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from .filename_formatter import get_basic_filename


def download_assets(url, directory):
    request = requests.get(url)
    html = BeautifulSoup(request.text, "html.parser")

    images = html.findAll("img")
    links = html.findAll("link")
    scripts = html.findAll("script")
    tags = images + links + scripts
    links = get_links(tags)

    for link in links:

        if is_same_domain(url, link):
            _, extension = os.path.splitext(link)
            asset_url = urljoin(url, link)
            asset_name = get_basic_filename(asset_url) + extension
            asset_path = os.path.join(directory, asset_name)

            with open(asset_path, "wb") as handler:
                asset_data = requests.get(asset_url).content
                handler.write(asset_data)


def is_same_domain(html_url, asset_url):
    parsed_asset_url = urlparse(asset_url)
    parsed_html_url = urlparse(html_url)
    asset_netloc = parsed_asset_url.netloc.strip("www.")
    html_netloc = parsed_html_url.netloc.strip("www.")
    _, extension = os.path.splitext(asset_url)
    if asset_netloc == html_netloc or asset_netloc == "":
        return True
    return False


def get_links(tags):
    tags_with_href = list(filter(lambda t: t.has_attr("href"), tags))
    tags_with_src = list(filter(lambda t: t.has_attr("src"), tags))
    href_links = []
    src_links = []
    for href_tag in tags_with_href:
        href_links.append(href_tag.get("href"))
    for src_tag in tags_with_src:
        src_links.append(src_tag.get("src"))

    return href_links + src_links

