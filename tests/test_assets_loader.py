import os
import requests_mock
from urllib.parse import urljoin
from page_loader import download_assets
from page_loader import build_fixture_path
from page_loader import get_basic_filename
from page_loader.html_formatter import get_extension

TEST_URL = "https://ru.hexlet.io/courses"
TEST_IMAGE_URL = "/assets/professions/nodejs.png"
TEST_CSS_URL = "/assets/application.css"
TEST_JS_SCRIPT_URL = "https://ru.hexlet.io/packs/js/runtime.js"
TEST_IMAGE = urljoin(TEST_URL, TEST_IMAGE_URL)
TEST_CSS = urljoin(TEST_URL, TEST_CSS_URL)
TEST_JS_SCRIPT = urljoin(TEST_URL, TEST_JS_SCRIPT_URL)


def build_asset_name(url):
    return get_basic_filename(url) + get_extension(url)


def test_download_assets(tmpdir):
    with requests_mock.Mocker() as mock:
        with open(build_fixture_path("test_html.html"), "r") as test_html, \
                open(build_fixture_path("test_image.png"), "rb") as test_image, \
                open(build_fixture_path("test_style.css"), "r") as test_css, \
                open(build_fixture_path("test_js_script.js"), "r") as test_js_script:
            path_to_image = os.path.join(tmpdir, build_asset_name(TEST_IMAGE))
            path_to_stylesheet = os.path.join(tmpdir, build_asset_name(TEST_CSS))
            path_to_js_script = os.path.join(tmpdir, build_asset_name(TEST_JS_SCRIPT))
            download_info = [
                (TEST_IMAGE, path_to_image),
                (TEST_CSS, path_to_stylesheet),
                (TEST_JS_SCRIPT, path_to_js_script)
            ]
            mock.get(TEST_URL, text=test_html.read())
            mock.get(TEST_IMAGE, content=test_image.read())
            mock.get(TEST_CSS, text=test_css.read())
            mock.get(TEST_JS_SCRIPT, text=test_js_script.read())
            download_assets(download_info)

            assert os.path.isfile(path_to_image)
            assert os.path.isfile(path_to_stylesheet)
            assert os.path.isfile(path_to_js_script)
