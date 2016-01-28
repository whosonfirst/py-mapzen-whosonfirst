#!/usr/bin/env python

import sys
import os
import shutil
import logging
import json

if __name__ == '__main__':

    import optparse
    opt_parser = optparse.OptionParser()

    opt_parser.add_option('--source', dest='source', action='store', default='/usr/local/mapzen', help='...')
    opt_parser.add_option('--strict', dest='strict', action='store_true', default=False, help='...')
    opt_parser.add_option('--out', dest='out', action='store', default=None, help='...')

    opt_parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Be chatty (default is false)')
    options, args = opt_parser.parse_args()

    if options.verbose:	
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    out = sys.stdout

    whoami = os.path.abspath(sys.argv[0])
    scripts = os.path.dirname(whoami)
    root = os.path.dirname(scripts)
    
    requires = os.path.join(root, "MAPZEN.REQUIRES.txt")
    fh = open(requires, "r")

    deps = {}

    for pkg in fh.readlines():

        pkg = pkg.strip()

        if pkg.startswith("#"):
            logging.debug("skipping '%s'" % pkg)
            continue

        py_pkg = pkg.replace(".", "-")
        py_pkg = "py-%s" % py_pkg

        pkg_path = os.path.join(options.source, py_pkg)

        if not os.path.exists(pkg_path):
            logging.error("can not find source for %s (%s)" % (pkg, pkg_path))

            if options.strict:
                sys.exit(1)

            continue

        version_path = os.path.join(pkg_path, "VERSION")

        if not os.path.exists(version_path):
            logging.error("can not find version for %s (%s)" % (pkg, version_path))

            if options.strict:
                sys.exit(1)

            continue
        
        pkg_fh = open(version_path, "r")
        pkg_version = pkg_fh.read()
        pkg_version = pkg_version.strip()

        pkg_str = "%s>=%s" % (pkg, pkg_version)
        pkg_link = "https://github.com/whosonfirst/%s/tarball/master#egg=%s-%s" % (py_pkg, pkg, pkg_version)

        deps[pkg_str] = pkg_link

    if options.out:

        if os.path.exists(options.out):
            bak = "%s.bak" % options.out
            shutil.copy(options.out, bak)

        out = open(options.out, 'w')

    json.dump(deps, out, indent=1)
    sys.exit(0)
