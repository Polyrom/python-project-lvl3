import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .filename_formatter import get_basic_filename
from .assets_loader import is_same_domain


def format_html(url, text, directory):
    html = BeautifulSoup(text, "html.parser")
    images = html.findAll("img")
    for image in images:
        image_link = image.get("src")
        _, extension = os.path.splitext(image_link)
        if is_same_domain(url, image_link) is not None:
            img_url = urljoin(url, image_link)
            image_name = get_basic_filename(img_url) + extension
            image["src"] = os.path.join(directory, image_name)

    return html.prettify()
