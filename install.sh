#!/bin/sh

UTILS='/usr/local/mapzen/py-mapzen-whosonfirst-utils'

USER_UTILS=$1

if [ "${USER_UTILS}" != "" ]
then 
    UTILS=$USER_UTILS
fi

if [ -d ${UTILS} ]
then
    echo "I can't find py-mapzen-whosonfirst-utils!"
    exit 1
fi

sudo python setup.py install


cd $UTILS
sudo python setup.py install
cd -

exit 0