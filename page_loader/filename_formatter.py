import os
import re
from urllib.parse import urlparse


def format_filename(url):
    split_url = urlparse(url)
    no_scheme_url = split_url._replace(scheme="").geturl()[2:]
    path, _ = os.path.splitext(no_scheme_url)
    filename = re.sub("[^A-Za-z0-9]", "-", path)
    return filename + ".html"

