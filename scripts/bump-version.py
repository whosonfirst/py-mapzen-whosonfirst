#!/usr/bin/env python

import sys
import os
import logging

if __name__ == '__main__':

    import optparse
    opt_parser = optparse.OptionParser()

    opt_parser.add_option('--increment', dest='increment', action='store', default='0.01', help='...')

    opt_parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Be chatty (default is false)')
    options, args = opt_parser.parse_args()

    if options.verbose:	
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    whoami = os.path.abspath(sys.argv[0])
    scripts = os.path.dirname(whoami)
    root = os.path.dirname(scripts)

    version = os.path.join(root, "VERSION")
    fh = open(version, "r")

    version = fh.read()
    version = version.strip()

    version = float(version)
    incr = float(options.increment)

    next = version + incr

    print next
    sys.exit(0)
