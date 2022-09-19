from page_loader import format_html
from page_loader import build_fixture_path

TEST_URL = "https://ru.hexlet.io/courses"


def test_format_html():
    with open(build_fixture_path("test_html.html")) as test_html, \
            open(build_fixture_path("expected_html.html")) as expected_html:
        assets_dir_name = "ru-hexlet-io-courses_files"
        resulting_html, _ = format_html(TEST_URL, test_html, assets_dir_name)
        assert resulting_html == expected_html.read()
