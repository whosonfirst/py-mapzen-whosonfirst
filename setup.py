#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(
    name='mapzen.whosonfirst',
    namespace_packages=[],
    version=version,
    description='A package to install all the other Who\'s On First Python packages',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst',
    install_requires=[
        'mapzen.whosonfirst.bundles>=0.03',
        'mapzen.whosonfirst.concordances>=0.06',
        'mapzen.whosonfirst.diff>=0.01',
        'mapzen.whosonfirst.export>=0.71',
        'mapzen.whosonfirst.geojson>=0.06',
        'mapzen.whosonfirst.languages>=0.02',
        'mapzen.whosonfirst.mapshaper>=0.04',
        'mapzen.whosonfirst.meta>=0.09',
        'mapzen.whosonfirst.names>=0.02',
        'mapzen.whosonfirst.pip>=0.03',
        'mapzen.whosonfirst.placetypes>=0.11',
        'mapzen.whosonfirst.search>=0.12',
        'mapzen.whosonfirst.sources>=0.03',
        'mapzen.whosonfirst.spatial>=0.12',
        'mapzen.whosonfirst.utils>=0.20',
        "mapzen.whosonfirst.validator>=0.10",
        "mapzen.whosonfirst.chatterbox>=0.01",
        "mapzen.whosonfirst.aws>=0.02",
        "slack.api>=0.04",
        ],
    dependency_links=[
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-bundles/tarball/master#egg=mapzen.whosonfirst.bundles-0.03',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-concordances/tarball/master#egg=mapzen.whosonfirst.concordances-0.06',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-diff/tarball/master#egg=mapzen.whosonfirst.diff-0.01',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-export/tarball/master#egg=mapzen.whosonfirst.export-0.71',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-geojson/tarball/master#egg=mapzen.whosonfirst.geojson-0.06',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-languages/tarball/master#egg=mapzen.whosonfirst.languages-0.02',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-mapshaper/tarball/master#egg=mapzen.whosonfirst.mapshaper-0.04',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-meta/tarball/master#egg=mapzen.whosonfirst.meta-0.09',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-names/tarball/master#egg=mapzen.whosonfirst.names-0.02',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-pip/tarball/master#egg=mapzen.whosonfirst.pip-0.03',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes/tarball/master#egg=mapzen.whosonfirst.placetypes-0.11',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-search/tarball/master#egg=mapzen.whosonfirst.search-0.12',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-sources/tarball/master#egg=mapzen.whosonfirst.sources-0.03',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-spatial/tarball/master#egg=mapzen.whosonfirst.spatial-0.12',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-utils/tarball/master#egg=mapzen.whosonfirst.utils-0.20',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-validator/tarball/master#egg=mapzen.whosonfirst.validator-0.10',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-chatterbox/tarball/master#egg=mapzen.whosonfirst.chatterbox-0.01',
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-aws/tarball/master#egg=mapzen.whosonfirst.aws-0.02',
        'https://github.com/whosonfirst/py-slack-api/tarball/master#egg=slack.api-0.04',
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst/releases/tag/' + version,
    license='BSD')
