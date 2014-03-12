# -*- coding: utf-8 -*-
# vim: expandtab shiftwidth=4 softtabstop=4
"""
    zgeist.conf
    ~~~~~~~~~~~

    zgeist configuration module
"""

import yaml

from util import approot, pp

from os.path import join, dirname, abspath, realpath
from glob import glob

class Config(object):
    """Loads configuration files, provides accessor methods.

    ZG configuration files are put into /conf/*.yaml where they
    are discovered, loaded and merged into one configuration.
    """
    def __init__(self, **opts):
        self.conf = {}
        if 'path' in opts:
            path = opts['path']
        else:
            path = approot('conf')

        files = sorted(glob(join(path, '*.yaml')))
        files.reverse()
        for f in [open(x) for x in files]:
            contents = f.read()
            contents = contents.replace('%APP%', approot())
            self.conf.update(yaml.load(contents))

    def __getitem__(self, key):
        try:
            return reduce(lambda d, k: d[k], key.split('.'), self.conf)
        except:
            return None

config = Config()

