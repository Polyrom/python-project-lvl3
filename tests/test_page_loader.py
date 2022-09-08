import os
import tempfile
import requests_mock
from urllib.parse import urljoin
from page_loader import download

TEST_URL = "https://ru.hexlet.io/courses"
TEST_IMAGE_URL = "/assets/professions/nodejs.png"
TEST_IMAGE = urljoin(TEST_URL, TEST_IMAGE_URL)


def fixture_path(filename):
    return os.path.join("tests", "fixtures", filename)


def test_page_loader():
    with requests_mock.Mocker() as m, tempfile.TemporaryDirectory() as td:
        with open(fixture_path("test_html.html"), "r") as test_html,\
                open(fixture_path("test_image.png"), "rb") as test_image:
            m.get(TEST_URL, text=test_html.read())
            m.get(TEST_IMAGE, content=test_image.read())
            path_to_html = os.path.join(td, "ru-hexlet-io-courses.html")
            assert download(TEST_URL, td) == path_to_html

            assert os.path.isfile(path_to_html)