import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from .filename_formatter import get_basic_filename


def download_images(url, directory):
    request = requests.get(url)
    html = BeautifulSoup(request.text, "html.parser")
    images = html.findAll("img")
    for image in images:
        image_link = image.get("src")
        _, extension = os.path.splitext(image_link)
        if is_image_correct(url, image_link):
            img_url = urljoin(url, image_link)
            image_name = get_basic_filename(img_url) + extension
            image_path = os.path.join(directory, image_name)
            with open(image_path, "wb") as handler:
                img_data = requests.get(img_url).content
                handler.write(img_data)


def is_image_correct(html_url, image_url):
    parsed_image_url = urlparse(image_url)
    parsed_html_url = urlparse(html_url)
    image_netloc = parsed_image_url.netloc.strip("www.")
    html_netloc = parsed_html_url.netloc.strip("www.")
    _, extension = os.path.splitext(image_url)
    if (image_netloc == html_netloc or image_netloc == "") and \
            (extension == ".jpg" or extension == ".png"):
        return True
    return False
