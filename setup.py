#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from patolabor import __author__, __version__, __license__

setup(
	name = 'patolabor',
	version = __version__,
	description = 'Python module for observing file events',
	license = __license__,
	author = __author__,
	author_email = 'sheema.sheemap@gmail.com',
	url = 'https://github.com/DaikiShimada/patolabor-python.git',
	keywords = 'filewatch filevent file monitoring python',
	packages = find_packages(),
	install_requires = [],
)
