from page_loader.filename_builder import build_basic_filepath

TEST_URL = "https://ru.hexlet.io/courses"


def test_build_basic_filepath():
    assert build_basic_filepath(TEST_URL) == "ru-hexlet-io-courses"
