import re
from urllib.parse import urlparse


def build_basic_filepath(url):
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme + "://"
    no_scheme_url = parsed_url.geturl().replace(scheme, "")
    path = no_scheme_url.strip("/")
    filepath = re.sub("[^A-Za-z0-9]", "-", path)

    return filepath
