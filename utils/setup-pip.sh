#!/bin/sh

# >>> import sys
# >>> print "\n".join(sys.path)
# 
# /usr/local/lib/python2.7/dist-packages/mapzen.whosonfirst-0.37-py2.7.egg
# /usr/local/lib/python2.7/dist-packages/mapzen.whosonfirst.search-0.13_-py2.7.egg
# and so on...

sudo apt-get update --fix-missing

sudo apt-get install -y libssl-dev libffi-dev libpython-dev
sudo apt-get install -y python-pip python-pyparsing python-setuptools

sudo python -m pip install --upgrade --force pip
sudo pip install --upgrade setuptools
sudo pip install --upgrade pyopenssl ndg-httpsclient pyasn1 'requests[security]'


