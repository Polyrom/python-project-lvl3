import os
import requests
import requests_mock
import tempfile
from urllib.parse import urljoin
from page_loader import download_assets

TEST_URL = "https://ru.hexlet.io/courses"
TEST_IMAGE_URL = "/assets/professions/nodejs.png"
TEST_CSS_URL = "/assets/application.css"
TEST_JS_SCRIPT_URL = "https://ru.hexlet.io/packs/js/runtime.js"
TEST_IMAGE = urljoin(TEST_URL, TEST_IMAGE_URL)
TEST_CSS = urljoin(TEST_URL, TEST_CSS_URL)
TEST_JS_SCRIPT = urljoin(TEST_URL, TEST_JS_SCRIPT_URL)


def fixture_path(filename):
    return os.path.join("tests", "fixtures", filename)


def test_download_assets():

    with requests_mock.Mocker() as m, tempfile.TemporaryDirectory() as td:
        with open(fixture_path("test_html.html"), "r") as test_html, \
                open(fixture_path("test_image.png"), "rb") as test_image, \
                open(fixture_path("test_style.css"), "r") as test_css, \
                open(fixture_path("test_js_script.js"), "r") as test_js_script:
            m.get(TEST_URL, text=test_html.read())
            m.get(TEST_IMAGE, content=test_image.read())
            m.get(TEST_CSS, text=test_css.read())
            m.get(TEST_JS_SCRIPT, text=test_js_script.read())
            pseudo_req = requests.get(TEST_URL)
            download_assets(TEST_URL, pseudo_req.text, td)
            path_to_image = os.path.join(td, "ru-hexlet-io-assets-professions-nodejs.png")
            path_to_stylesheet = os.path.join(td, "ru-hexlet-io-assets-application.css")
            path_to_js_script = os.path.join(td, "ru-hexlet-io-packs-js-runtime.js")

            assert os.path.isfile(path_to_image)
            assert os.path.isfile(path_to_stylesheet)
            assert os.path.isfile(path_to_js_script)
