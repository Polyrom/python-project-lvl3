import os
from page_loader.page_loader import download
from page_loader.assets_loader import download_assets
from page_loader.filename_formatter import get_basic_filename
from page_loader.html_formatter import format_html


def build_fixture_path(filename):
    return os.path.join("tests", "fixtures", filename)


__all__ = [
    'download',
    'download_assets',
    'get_basic_filename',
    'format_html',
    'build_fixture_path'
]
