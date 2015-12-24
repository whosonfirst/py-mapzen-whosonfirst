#!/bin/sh

# THIS IS A TOTAL HACK. IT IS NOT A FEATURE. IT WILL BE FIXED SOON. UNLESS IT'S JUST
# ONE OF THOSE THINGS. WHICH IS POSSIBLE, RIGHT? BECAUSE COMPUTERS...
#
# For reasons I do NOT understand anytime a py-mapzen-whosonfirst package is installed
# then Python helpfully replaces 'mapzen.whosonfirst.utils' with an old version. Of
# course that pacakge is used by everything else so hilarity ensues. This is a helpful
# shell script to automate to need to re-install py-mapzen-whosonfirst-utils. It assumes
# the source code lives at '/usr/local/mapzen/py-mapzen-whosonfirst-utils' but you can
# change this by passing your path (for the source) as the one and only argument to the
# shell script. Good times... (20151223/thisisaaronland)

UTILS='/usr/local/mapzen/py-mapzen-whosonfirst-utils'

USER_UTILS=$1

if [ "${USER_UTILS}" != "" ]
then 
    UTILS=$USER_UTILS
fi

if [ ! -d ${UTILS} ]
then
    echo "I can't find '${UTILS}'"
    exit 1
fi

sudo python setup.py install

cd $UTILS
sudo python setup.py install
cd -

exit 0
