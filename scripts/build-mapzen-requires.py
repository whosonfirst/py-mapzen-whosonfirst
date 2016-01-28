#!/usr/bin/env python

import sys
import os
import logging
import json

if __name__ == '__main__':

    # please make me CLI options

    src="/usr/local/mapzen"
    strict = False
    out = sys.stdout

    # end of please make me CLI options

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

        pkg_path = os.path.join(src, py_pkg)

        if not os.path.exists(pkg_path):
            logging.error("can not find source for %s (%s)" % (pkg, pkg_path))

            if strict:
                sys.exit(1)

            continue

        version_path = os.path.join(pkg_path, "VERSION")

        if not os.path.exists(version_path):
            logging.error("can not find version for %s (%s)" % (pkg, version_path))

            if strict:
                sys.exit(1)

            continue
        
        pkg_fh = open(version_path, "r")
        pkg_version = pkg_fh.read()
        pkg_version = pkg_version.strip()

        pkg_str = "%s>=%s" % (pkg, pkg_version)
        pkg_link = "https://github.com/whosonfirst/%s/tarball/master#egg=%s-%s" % (py_pkg, pkg, pkg_version)

        deps[pkg_str] = pkg_link

    json.dump(deps, out, indent=1)
    sys.exit(0)
