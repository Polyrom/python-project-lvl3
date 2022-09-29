import os
import re
from urllib.parse import urlparse, urljoin


def build_basic_filepath(url):
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme + "://"
    no_scheme_url = parsed_url.geturl().replace(scheme, "")
    path = no_scheme_url.strip("/")
    filepath = re.sub("[^A-Za-z0-9]", "-", path)

    return filepath + ".html"


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
