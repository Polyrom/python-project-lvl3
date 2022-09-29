import os
import string
import random
import pytest
import requests.exceptions
import requests_mock
from tests import build_fixture_path
from page_loader import download
from page_loader.filename_builder import build_basic_filepath

ASSETS = [("https://ru.hexlet.io/courses", "test_html.html"),
          ("/assets/professions/nodejs.png", "test_image.png"),
          ("/assets/application.css", "test_style.css"),
          ("https://ru.hexlet.io/packs/js/runtime.js", "test_js_script.js")]


def get_random_string(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@pytest.mark.parametrize("test_url", ("https://ru.hexlet.io/courses",))
def test_page_loader(tmpdir, test_url):
    with requests_mock.Mocker() as mock:
        for url, fixture_name in ASSETS:
            with open(build_fixture_path(fixture_name), 'rb') as test_asset:
                mock.get(url, content=test_asset.read())

        path_to_html = os.path.join(tmpdir, build_basic_filepath(test_url) + ".html")
        assert download(url=test_url, output=tmpdir) == path_to_html
        assert os.path.isfile(path_to_html)


@pytest.mark.parametrize("random_url", ("something.org",))
def test_page_loader_invalid_dir(tmpdir, random_url):
    with pytest.raises(FileNotFoundError):
        random_filename = get_random_string()
        fake_directory_path = os.path.join(tmpdir, random_filename)
        download(url=random_url, output=fake_directory_path)


@pytest.mark.parametrize("test_url", ("https://ru.hexlet.io/courses",))
def test_page_loader_req_err(tmpdir, test_url):
    with pytest.raises(requests.exceptions.RequestException):
        with requests_mock.Mocker() as mock:
            mock.get(test_url, status_code=404)
            download(url=test_url, output=tmpdir)
