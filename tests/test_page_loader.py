import os
import string
import random
import pytest
import tempfile
import requests.exceptions
import requests_mock
from urllib.parse import urljoin
from page_loader import download
from page_loader.page_loader import create_assets_dir

TEST_URL = "https://ru.hexlet.io/courses"
TEST_IMAGE_URL = "/assets/professions/nodejs.png"
TEST_CSS_URL = "/assets/application.css"
TEST_JS_SCRIPT_URL = "https://ru.hexlet.io/packs/js/runtime.js"
TEST_IMAGE = urljoin(TEST_URL, TEST_IMAGE_URL)
TEST_CSS = urljoin(TEST_URL, TEST_CSS_URL)
TEST_JS_SCRIPT = urljoin(TEST_URL, TEST_JS_SCRIPT_URL)


def fixture_path(filename):
    return os.path.join("tests", "fixtures", filename)


def get_random_string(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def test_page_loader():
    with requests_mock.Mocker() as m, tempfile.TemporaryDirectory() as td:
        with open(fixture_path("test_html.html"), "r") as test_html,\
                open(fixture_path("test_image.png"), "rb") as test_image, \
                open(fixture_path("test_style.css"), "r") as test_css, \
                open(fixture_path("test_js_script.js"), "r") as test_js_script:

            m.get(TEST_URL, text=test_html.read())
            m.get(TEST_IMAGE, content=test_image.read())
            m.get(TEST_CSS, text=test_css.read())
            m.get(TEST_JS_SCRIPT, text=test_js_script.read())
            path_to_html = os.path.join(td, "ru-hexlet-io-courses.html")
            assert download(td, TEST_URL) == path_to_html
            assert os.path.isfile(path_to_html)


def test_page_loader_invalid_dir():
    with pytest.raises(FileNotFoundError):
        with tempfile.TemporaryDirectory() as td:
            random_url = "something.org"
            random_filename = get_random_string()
            fake_directory_path = os.path.join(td, random_filename)
            download(random_url, fake_directory_path)


def test_page_loader_req_err():
    with pytest.raises(requests.exceptions.RequestException):
        with requests_mock.Mocker() as m, tempfile.TemporaryDirectory() as td:
            m.get(TEST_URL, status_code=404)
            download(td, TEST_URL)


def test_create_assets_dir():
    with tempfile.TemporaryDirectory() as td:
        test_dir = os.path.join(td, "test_dir")
        os.mkdir(test_dir)
        create_assets_dir(test_dir)

        assert os.path.exists(test_dir)


