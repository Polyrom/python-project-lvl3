import os
import requests_mock
import tempfile
from page_loader import download

TEST_URL = "https://ru.hexlet.io/courses"


def test_download():
    with tempfile.TemporaryDirectory() as tempdir:
        with requests_mock.Mocker() as mock:
            mock.get(TEST_URL, text="something")
            expected_filename = os.path.join(tempdir, "ru-hexlet-io-courses.html")
            assert download(TEST_URL, tempdir) == expected_filename
            with open(os.path.join(tempdir, expected_filename)) as target_file:
                download(TEST_URL, tempdir)
                assert target_file.read() == "something"

