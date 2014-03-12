# -*- coding: utf-8 -*-
"""
    wsgi
    ~~~~

    zgeist wsgi module
"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from zgeist import frontend

application = DispatcherMiddleware(frontend.create_app())

if __name__ == "__main__":
    run_simple('10.0.0.1', 5000, application, use_reloader=True, use_debugger=True)

