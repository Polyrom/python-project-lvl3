import os
import pytest
import requests_mock
from urllib.parse import urljoin
from tests import build_fixture_path
from page_loader.assets_loader import download_assets, format_html
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
        download_assets(assets_info=download_info)
        assert os.path.isfile(path_to_asset)


@pytest.mark.parametrize("test_url, test_html, expected_html",
                         [("https://ru.hexlet.io/courses",
                          build_fixture_path("test_html.html"), build_fixture_path("expected_html.html"))])
def test_format_html(test_url, test_html, expected_html):
    with requests_mock.Mocker() as mock:
        with open(test_html) as test_html, open(expected_html) as expected_html:
            mock.get(test_url, text=test_html.read())
            filename = build_basic_filepath(test_url)
            resulting_html, _, _ = format_html(url=test_url,
                                               parent_dir="",
                                               filename=filename)
            assert resulting_html == expected_html.read()
