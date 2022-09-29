import os


def build_fixture_path(filename):
    return os.path.join("tests", "fixtures", filename)


__all__ = ['build_fixture_path']
