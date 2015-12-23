#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.bundle',
    namespace_packages=[],
    version='0.16',
    description='A package to install all the other Who\'s On First Python packages',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-bundle',
    install_requires=[
        'mapzen.whosonfirst.concordances>=0.05',
        'mapzen.whosonfirst.export>=0.68',
        'mapzen.whosonfirst.geojson>=0.06',
        'mapzen.whosonfirst.languages>=0.02',
        'mapzen.whosonfirst.mapshaper>=0.04',
        'mapzen.whosonfirst.names>=0.02',
        'mapzen.whosonfirst.placetypes>=0.10',
        'mapzen.whosonfirst.search>=0.11',
        'mapzen.whosonfirst.sources>=0.03',
        'mapzen.whosonfirst.spatial>=0.11',
        'mapzen.whosonfirst.utils>=0.17',
        "mapzen.whosonfirst.validator>=0.09",
        "mapzen.whosonfirst.chatterbox>=0.01",
        "mapzen.whosonfirst.aws>=0.01",
        ],
    dependency_links=[
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-concordances/tarball/master#egg=mapzen.whosonfirst.concordances-0.05',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-export/tarball/master#egg=mapzen.whosonfirst.export-0.68',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-geojson/tarball/master#egg=mapzen.whosonfirst.geojson-0.06',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-languages/tarball/master#egg=mapzen.whosonfirst.languages-0.02',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-mapshaper/tarball/master#egg=mapzen.whosonfirst.mapshaper-0.04',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-names/tarball/master#egg=mapzen.whosonfirst.names-0.02',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes/tarball/master#egg=mapzen.whosonfirst.placetypes-0.10',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-search/tarball/master#egg=mapzen.whosonfirst.search-0.11',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-sources/tarball/master#egg=mapzen.whosonfirst.sources-0.03',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-spatial/tarball/master#egg=mapzen.whosonfirst.spatial-0.11',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-utils/tarball/master#egg=mapzen.whosonfirst.utils-0.17',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-validator/tarball/master#egg=mapzen.whosonfirst.validator-0.09',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-chatterbox/tarball/master#egg=mapzen.whosonfirst.chatterbox-0.01',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-aws/tarball/master#egg=mapzen.whosonfirst.aws-0.01',
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-bundle/releases/tag/v0.16',
    license='BSD')
