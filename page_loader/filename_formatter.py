import os
import re
from urllib.parse import urlparse


def get_basic_filename(url):
    split_url = urlparse(url)
    scheme = split_url.scheme + "://"
    no_scheme_url = split_url.geturl().replace(scheme, "")
    path, _ = os.path.splitext(no_scheme_url)
    clean_path = path.strip("/")
    filename = re.sub("[^A-Za-z0-9]", "-", clean_path)

    return filename
