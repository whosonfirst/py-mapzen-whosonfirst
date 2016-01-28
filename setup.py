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

# See also: scripts/build-mapzen-requires.py

import json

# please to list your not-MAPZEN.REQUIRES.txt dependencies here - the format is
# "<PACKAGE> and optional versioning" + ":" + "optional dependency/install link"
# py-mapzen specific stuff is handled separately afterwards by reading the
# MAPZEN.REQUIRES.json file (20160128/thisisaaronland)

deps = {
    'slack.api>=0.04':'https://github.com/whosonfirst/py-slack-api/tarball/master#egg=slack.api-0.04'
}

requires=[]
links=[]

mz_deps = os.path.join(parent, "MAPZEN.REQUIRES.json")

if not os.path.exists(mz_deps):
    raise Exception, "%s does not exist - please run scripts/build-mapzen-requires.py" % mz_deps

mz_fh = open(mz_deps, "r")
mz_data = json.load(mz_fh)

for pkg, url in mz_data.items():
    deps[pkg] = url

for pkg, url in deps.items():

    requires.append(pkg)

    if url != '':
        links.append(url)

# Okay... now we carry on as is...

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
    install_requires=requires,	# see above
    dependency_links=links,	# no really, see above
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst/releases/tag/' + version,
    license='BSD')
