import requests_mock
import pytest
from page_loader.html_formatter import format_html
from page_loader.url import build_basic_filepath
from tests import build_fixture_path


@pytest.mark.parametrize("test_url, test_html, expected_html",
                         [("https://ru.hexlet.io/courses",
                          build_fixture_path("test_html.html"), build_fixture_path("expected_html.html"))])
def test_format_html(test_url, test_html, expected_html):
    with requests_mock.Mocker() as mock:
        with open(test_html) as test_html, open(expected_html) as expected_html:
            mock.get(test_url, text=test_html.read())
            filename = build_basic_filepath(test_url)
            resulting_html, _ = format_html(url=test_url,
                                            parent_dir="",
                                            filename=filename)
            assert resulting_html == expected_html.read()
