
[![linter-check](https://github.com/Polyrom/python-project-lvl3/actions/workflows/linter-check.yml/badge.svg)](https://github.com/Polyrom/python-project-lvl3/actions/workflows/linter-check.yml) [![pytest-check](https://github.com/Polyrom/python-project-lvl3/actions/workflows/pytest-check.yml/badge.svg)](https://github.com/Polyrom/python-project-lvl3/actions/workflows/pytest-check.yml) [![Actions Status](https://github.com/Polyrom/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/Polyrom/python-project-lvl3/actions) <a href="https://codeclimate.com/github/Polyrom/python-project-lvl3/maintainability"><img src="https://api.codeclimate.com/v1/badges/f483fc3569edc6fd01b2/maintainability" /></a> <a href="https://codeclimate.com/github/Polyrom/python-project-lvl3/test_coverage"><img src="https://api.codeclimate.com/v1/badges/f483fc3569edc6fd01b2/test_coverage" /></a>

# Page loader
A nice CLI utility to download any Internet page to view it offline later.

### Installation
Just clone this repo to your machine, go to the package directory and run the following command in your terminal:

`make package-install`

### Getting started
To download an Internet page locally, run:

`page-loader [URL here]`

By default, the HTML file will be saved to the current working directory.

If you wish to set the destination directory, run:

`page-loader [URL] -o [PATH TO DIRECTORY]`

Alternatively, you can replace the `-o` flag with `--output`.

You may always run `page-loader -h` to see the options in your console.

### How it works
[![asciicast](https://asciinema.org/a/JaGFmCzBmyZScPb6NMSbaYDsD.svg)](https://asciinema.org/a/JaGFmCzBmyZScPb6NMSbaYDsD)