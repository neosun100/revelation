#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''revelation setup file'''

import os
import re

from setuptools import find_packages, setup

try:
    import pypandoc
    README = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    README = ''

# package variables
PACKAGE = 'revelation'
REQUIREMENTS = [
    'Jinja2==2.10',
    'Werkzeug==0.14.1',
    'click==6.7',
]
TEST_REQUIREMENTS = [
    'coverage==4.4.1',
    'coveralls==1.1',
    'nose==1.3.7',
    'pylint==1.7.1',
]

# dynamic package info
with open(os.path.join(PACKAGE, '__init__.py')) as init_file:
    INIT = init_file.read()

VERSION = re.search(
    "^__version__ = ['\"]([^'\"]+)['\"]", INIT, re.MULTILINE).group(1)
AUTHOR = re.search(
    "^__author__ = ['\"]([^'\"]+)['\"]", INIT, re.MULTILINE).group(1)
EMAIL = re.search(
    "^__email__ = ['\"]([^'\"]+)['\"]", INIT, re.MULTILINE).group(1)

setup(
    name=PACKAGE,
    version=VERSION,
    description='Make awesome reveal.js presentations with revelation',
    long_description=README,
    author=AUTHOR,
    author_email=EMAIL,
    url='https://github.com/humrochagf/revelation',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    entry_points=dict(
        console_scripts=['revelation=revelation.cli:cli']),
    platforms='any',
    keywords=['presentation', 'slides', 'reveal.js', 'markdown'],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
    extras_require={'test': TEST_REQUIREMENTS}
)
