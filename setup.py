#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.bundle',
    namespace_packages=[],
    version='0.01',
    description='A package to install all the other Who\'s On First Python packages',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-bundle',
    install_requires=[
        'mapzen.whosonfirst.concordances',
        'mapzen.whosonfirst.export',
        'mapzen.whosonfirst.geojson',
        'mapzen.whosonfirst.languages',
        'mapzen.whosonfirst.mapshaper',
        'mapzen.whosonfirst.names',
        'mapzen.whosonfirst.placetypes',
        'mapzen.whosonfirst.search',
        'mapzen.whosonfirst.spatial',
        'mapzen.whosonfirst.utils',
        'mapzen.whosonfirst.validator'
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-bundle/releases/tag/v0.01',
    license='BSD')
