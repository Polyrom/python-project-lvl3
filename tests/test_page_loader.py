import os
import string
import random
import pytest
import tempfile
import requests.exceptions
import requests_mock
from urllib.parse import urljoin
from page_loader import download
from page_loader import build_fixture_path
from page_loader import get_basic_filename


TEST_URL = "https://ru.hexlet.io/courses"
TEST_IMAGE_URL = "/assets/professions/nodejs.png"
TEST_CSS_URL = "/assets/application.css"
TEST_JS_SCRIPT_URL = "https://ru.hexlet.io/packs/js/runtime.js"
TEST_IMAGE = urljoin(TEST_URL, TEST_IMAGE_URL)
TEST_CSS = urljoin(TEST_URL, TEST_CSS_URL)
TEST_JS_SCRIPT = urljoin(TEST_URL, TEST_JS_SCRIPT_URL)
ASSETS = [(TEST_URL, "test_html.html", "r"),
          (TEST_IMAGE_URL, "test_image.png", "rb"),
          (TEST_CSS_URL, "test_style.css", "r"),
          (TEST_JS_SCRIPT_URL, "test_js_script.js", "r")]


def get_random_string(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def test_page_loader(tmpdir):
    with requests_mock.Mocker() as mock:
        for url, fixture_name, code in ASSETS:
            with open(build_fixture_path(fixture_name), code) as test_asset:
                if code == "rb":
                    mock.get(url, content=test_asset.read())
                else:
                    mock.get(url, text=test_asset.read())

        path_to_html = os.path.join(tmpdir, get_basic_filename(TEST_URL) + ".html")
        assert download(url=TEST_URL, output=tmpdir) == path_to_html
        assert os.path.isfile(path_to_html)


def test_page_loader_invalid_dir(tmpdir):
    with pytest.raises(FileNotFoundError):
        random_url = "something.org"
        random_filename = get_random_string()
        fake_directory_path = os.path.join(tmpdir, random_filename)
        download(url=random_url, output=fake_directory_path)


def test_page_loader_req_err():
    with pytest.raises(requests.exceptions.RequestException):
        with requests_mock.Mocker() as m, tempfile.TemporaryDirectory() as td:
            m.get(TEST_URL, status_code=404)
            download(url=TEST_URL, output=td)
