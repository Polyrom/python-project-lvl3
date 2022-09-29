import pytest
from page_loader.url import build_basic_filepath


@pytest.mark.parametrize("test_url", ("https://ru.hexlet.io/courses",))
def test_build_basic_filepath(test_url):
    assert build_basic_filepath(test_url) == "ru-hexlet-io-courses.html"
