# -*- coding: utf-8 -*-
# vim: expandtab shiftwidth=4 softtabstop=4
"""
    zgeist.util
    ~~~~~~~~~~~

    zgeist utilities
"""

import pkgutil
import importlib

from flask import Blueprint
import os
import sys
import base64
import random
import urlparse
import urllib
import pprint

from os.path import join, dirname, abspath, realpath

def approot(*prefix):
    return realpath(join(dirname(abspath(__file__)), '..', *prefix))

def pp(obj):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(obj)

def url_merge_param(url, params={}):
    """Returns a url with the specified params merged."""
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urllib.urlencode(query)
    return urlparse.urlunparse(url_parts)

def get_random_string():
    """Returns an impossible to guess random string."""
    return base64.urlsafe_b64encode(str(random.getrandbits(128))).replace('=','')

def tail( f, window=20 ):
    BUFSIZ = 1024
    f.seek(0, 2)
    bytes = f.tell()
    size = window
    block = -1
    data = []
    while size > 0 and bytes > 0:
        if (bytes - BUFSIZ > 0):
            # Seek back one whole BUFSIZ
            f.seek(block*BUFSIZ, 2)
            # read BUFFER
            data.append(f.read(BUFSIZ))
        else:
            # file too small, start from begining
            f.seek(0,0)
            # only read what was not read
            data.append(f.read(bytes))
        linesFound = data[-1].count('\n')
        size -= linesFound
        bytes -= BUFSIZ
        block -= 1
    return '\n'.join(''.join(data).splitlines()[-window:])

def levenshtein(seq1, seq2):
    oneago = None
    thisrow = range(1, len(seq2) + 1) + [0]
    for x in xrange(len(seq1)):
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
        for y in xrange(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
    return thisrow[len(seq2) - 1]

def mkdirs(path):
    """Create all directories of path."""
    dirs = os.path.realpath(path)
    dirs = os.path.dirname(dirs)
    a = []
    for seg in dirs.split('/'):
        a.append(seg)
        if len(a) > 1:
            cdir = '/'.join(a)
            if not os.path.exists(cdir):
                os.mkdir(cdir)

def resolve_absolute(path, *prefixes):
    """Returns the absolute path from a relative/absolute.
    Uses the app path as cwd for relative paths.

    ~/rbot => /home/apoc/rbot
    ./foo  => /home/apoc/projects/python/vereind/foo
    /tmp   => /tmp
    /tmp, ./foo => /tmp/foo
    etc.
    """
    path = os.path.expanduser(path) # ~ => /home/apoc
    if path[0] != '/': # resolve relative path, with app cwd as root
        path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), '..', path)

    path = os.path.join(path, *prefixes)
    path = os.path.realpath(path)

    return path

def register_blueprints(app, package_name, package_path):
    """Register all Blueprint instances on the specified Flask application found
    in all modules for the specified package.

    :param app: the Flask application
    :param package_name: the package name
    :param package_path: the package path
    """
    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv

