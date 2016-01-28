#!/usr/bin/env python

import sys
import os
import shutil
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
    backup = os.path.join(root, "VERSION.bak")

    fh = open(version, "r")
    current = fh.read()
    fh.close()

    current = current.strip()

    current = float(current)
    incr = float(options.increment)

    next = current + incr

    shutil.copy(version, backup)

    out = open(version, "w")
    out.write("%.02f" % next)
    out.close()

    sys.exit(0)
