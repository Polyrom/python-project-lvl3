import pytest
from page_loader.url import build_basic_filepath, is_same_domain, build_asset_name


@pytest.mark.parametrize("test_url", ("https://ru.hexlet.io/courses",))
def test_build_basic_filepath(test_url):
    assert build_basic_filepath(test_url) == "ru-hexlet-io-courses.html"


@pytest.mark.parametrize("url_same, url_no_netloc, url_different, test_url",
                         [("https://ru.hexlet.io/media",
                           "/courses/image.png",
                           "https://something.org/assets",
                           "https://ru.hexlet.io/courses")])
def test_is_same_domain(test_url, url_same, url_different, url_no_netloc):
    assert is_same_domain(test_url, url_same)
    assert is_same_domain(test_url, url_no_netloc)
    assert is_same_domain(test_url, url_different) is False


@pytest.mark.parametrize("test_url, asset_link, result",
                         [("https://ru.hexlet.io/courses",
                           "/assets/professions/nodejs.png",
                           "ru-hexlet-io-assets-professions-nodejs.png")])
def test_build_asset_name(test_url, asset_link, result):
    assert build_asset_name(test_url, asset_link) == result
