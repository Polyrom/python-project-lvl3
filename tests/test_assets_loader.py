import os
import pytest
import requests_mock
from urllib.parse import urljoin
from tests import build_fixture_path
from page_loader.assets_loader import download_assets
from page_loader.url import build_basic_filepath

ASSETS = [
    ("https://ru.hexlet.io/courses", "test_html.html"),
    ("/assets/professions/nodejs.png", "test_image.png"),
    ("/assets/application.css", "test_style.css"),
    ("https://ru.hexlet.io/packs/js/runtime.js", "test_js_script.js")
]


def build_asset_name(url):
    _, ext = os.path.splitext(url)
    extension = ".html" if ext == "" else ext
    return build_basic_filepath(url) + extension


@pytest.mark.parametrize("test_url", ("https://ru.hexlet.io/courses",))
def test_download_assets(tmpdir, test_url):
    with requests_mock.Mocker() as mock:
        for url, fixture_name in ASSETS:
            with open(build_fixture_path(fixture_name), "rb") as test_asset:
                test_asset_url = urljoin(test_url, url)
                path_to_asset = os.path.join(tmpdir, build_asset_name(test_asset_url))
                download_info = [(test_asset_url, path_to_asset)]
                mock.get(url, content=test_asset.read())
        download_assets(assets_info=download_info,
                        parent_dir=tmpdir,
                        filename=build_basic_filepath(test_url))
        assert os.path.isfile(path_to_asset)
