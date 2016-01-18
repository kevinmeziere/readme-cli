#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name = "readme-get",
    version = "0.1",
    packages = find_packages(),
    install_requires = ['beautifulsoup4>=4.4.1', 'requests>=2.9.1'],
    author = "Kevin Meziere",
    author_email = "kevin@project-fifo.net",
    description = "A simple tool to download a project from readme.io",
    license = "MIT",
)