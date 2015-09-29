#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.bundle',
    namespace_packages=[],
    version='0.04',
    description='A package to install all the other Who\'s On First Python packages',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-bundle',
    install_requires=[
        'mapzen.whosonfirst.concordances>=0.01',
        'mapzen.whosonfirst.export>=0.6',
        'mapzen.whosonfirst.geojson>0.03',
        'mapzen.whosonfirst.languages>=0.02',
        'mapzen.whosonfirst.mapshaper>=0.01',
        'mapzen.whosonfirst.names>=0.02',
        'mapzen.whosonfirst.placetypes>=0.04',
        'mapzen.whosonfirst.search>=0.03',
        'mapzen.whosonfirst.spatial>=0.03',
        'mapzen.whosonfirst.utils>=0.05',
        'mapzen.whosonfirst.validator>=0.04'
        ],
    dependency_links=[
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-concordances/tarball/master#egg=mapzen.whosonfirst.concordances',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-export/tarball/master#egg=mapzen.whosonfirst.export',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-geojson/tarball/master#egg=mapzen.whosonfirst.geojson',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-labels/tarball/master#egg=mapzen.whosonfirst.labels',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-languages/tarball/master#egg=mapzen.whosonfirst.languages',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-mapshaper/tarball/master#egg=mapzen.whosonfirst.mapshaper',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-names/tarball/master#egg=mapzen.whosonfirst.names',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes/tarball/master#egg=mapzen.whosonfirst.placetypes',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-search/tarball/master#egg=mapzen.whosonfirst.search',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-spatial/tarball/master#egg=mapzen.whosonfirst.spatial',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-utils/tarball/master#egg=mapzen.whosonfirst.utils',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-validator/tarball/master#egg=mapzen.whosonfirst.validator',
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-bundle/releases/tag/v0.04',
    license='BSD')
