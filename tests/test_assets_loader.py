import os
import pytest
import requests_mock
from urllib.parse import urljoin
from tests import build_fixture_path
from page_loader.assets_loader import download_assets
from page_loader.filename_builder import build_basic_filepath

TEST_IMAGE = "/assets/professions/nodejs.png"
TEST_CSS = "/assets/application.css"
TEST_JS_SCRIPT = "https://ru.hexlet.io/packs/js/runtime.js"


def build_asset_name(url):
    _, ext = os.path.splitext(url)
    extension = ".html" if ext == "" else ext
    return build_basic_filepath(url) + extension


@pytest.mark.parametrize("test_url", ("https://ru.hexlet.io/courses",))
def test_download_assets(tmpdir, test_url):
    with requests_mock.Mocker() as mock:
        with open(build_fixture_path("test_html.html"), "r") as test_html, \
                open(build_fixture_path("test_image.png"), "rb") as test_image, \
                open(build_fixture_path("test_style.css"), "r") as test_css, \
                open(build_fixture_path("test_js_script.js"), "r") as test_js_script:
            test_image_url = urljoin(test_url, TEST_IMAGE)
            test_css_url = urljoin(test_url, TEST_CSS)
            test_js_script_url = urljoin(test_url, TEST_JS_SCRIPT)
            path_to_image = os.path.join(tmpdir, build_asset_name(test_image_url))
            path_to_stylesheet = os.path.join(tmpdir, build_asset_name(test_css_url))
            path_to_js_script = os.path.join(tmpdir, build_asset_name(test_js_script_url))
            download_info = [
                (test_image_url, path_to_image),
                (test_css_url, path_to_stylesheet),
                (test_js_script_url, path_to_js_script)
            ]
            mock.get(test_url, text=test_html.read())
            mock.get(test_image_url, content=test_image.read())
            mock.get(test_css_url, text=test_css.read())
            mock.get(test_js_script_url, text=test_js_script.read())
            download_assets(assets_info=download_info,
                            parent_dir=tmpdir,
                            filename=build_basic_filepath(test_url))

            assert os.path.isfile(path_to_image)
            assert os.path.isfile(path_to_stylesheet)
            assert os.path.isfile(path_to_js_script)
