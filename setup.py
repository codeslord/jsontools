#!/usr/bin/env python

from setuptools import setup, find_packages

execfile('jsontools/version.py')

setup(
    name=__package_name__,
    version=__package_version__,
    description='Handy command line utilities for working with JSON',
    author='Will Ballard',
    author_email='wballard@mailfame.net',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'json = jsontools.cli:main'
        ]
    },
    requires=['docopt', 'clint', 'pystache'],
)
