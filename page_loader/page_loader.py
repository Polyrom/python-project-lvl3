import requests
import os
from .filename_formatter import format_filename


def download(url, output):
    r = requests.get(url)
    filename = format_filename(url)
    filepath = os.path.join(output, filename)
    with open(filepath, "w") as f:
        f.write(r.text)
    return filepath
