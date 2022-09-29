from page_loader.html_formatter import format_html
from page_loader.filename_builder import build_basic_filepath
from tests import build_fixture_path

TEST_URL = "https://ru.hexlet.io/courses"


def test_format_html():
    with open(build_fixture_path("test_html.html")) as test_html, \
            open(build_fixture_path("expected_html.html")) as expected_html:
        filename = build_basic_filepath(TEST_URL)
        resulting_html, _ = format_html(url=TEST_URL,
                                        text=test_html,
                                        parent_dir="",
                                        filename=filename)
        assert resulting_html == expected_html.read()
