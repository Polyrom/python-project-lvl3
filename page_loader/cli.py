import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(
        description="Downloads a webpage to your computer"
    )
    parser.add_argument("url")
    parser.add_argument(
        "--output",
        default=os.getcwd(),
        help="target directory"
    )
    return parser.parse_args()
