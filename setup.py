#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'osrsbox'
DESCRIPTION = 'A complete and up-to-date database of Old School RuneScape (OSRS) items.'
URL = 'https://github.com/osrsbox/osrsbox-db'
EMAIL = 'phoil@osrsbox.com'
AUTHOR = 'PH01L'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = "1.0.3"

# Name of any third party packages that are required from the `osrsbox` package.
REQUIRED = [
]

here = os.path.abspath(os.path.dirname(__file__))
readme_location = os.path.join(here, "osrsbox")

# Import the README and use it as the long-description.
with io.open(os.path.join(readme_location, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    include_package_data=True,
    license='GPLv3',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)