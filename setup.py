#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os
import sys
import shutil

setup = os.path.abspath(sys.argv[0])
parent = os.path.dirname(setup)
pkg = os.path.basename(parent)

if pkg.startswith("py-mapzen"):
    pkg = pkg.replace("py-", "")
    pkg = pkg.replace("-", ".")

    egg_info = "%s.egg-info" % pkg
    egg_info = os.path.join(parent, egg_info)

    if os.path.exists(egg_info):
        shutil.rmtree(egg_info)

# Okay carry on as usual... well, except for all the requires stuff
# below (20160128/thisisaaronland)

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
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst/releases/tag/' + version,
    license='BSD')
