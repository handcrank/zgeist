# -*- coding: utf-8 -*-
# vim: expandtab shiftwidth=4 softtabstop=4
"""
    zgeist.app
    ~~~~~~~~~~

    zgeist flask application
"""

from flask import Flask
from flask.ext.assets import Environment, Bundle

from .. import util

def create_app():
    app = Flask('zgeist',
        static_folder=util.approot('public'),
        template_folder=util.approot('view'))
    app.debug = True

    assets = Environment(app)
    assets.url = app.static_url_path

    css_bundle = Bundle('css/style.sass', filters='sass', output='gen/style.css')
    assets.register('css_all', css_bundle)

    js_bundle = Bundle('js/*.js', output='gen/packed.min.js')
    assets.register('js_all', js_bundle)

    # automagically discovers and loads all the
    # blueprints in the frontend package
    util.register_blueprints(app, __name__, __path__)

    return app

