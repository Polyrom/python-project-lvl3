from page_loader import get_basic_filename

TEST_URL = "https://ru.hexlet.io/courses"


def test_get_basic_filename():
    assert get_basic_filename(TEST_URL) == "ru-hexlet-io-courses"
