# -*- coding: utf-8 -*-
# vim: expandtab shiftwidth=4 softtabstop=4
"""
    zgeist.frontend.gallery
    ~~~~~~~~~~~~~~~~~~~~~~~

    gallery frontend, shows items
"""

from .. import Session
from ..models import Item

from flask import Blueprint, render_template

import logging
logger = logging.getLogger('zgeist')

bp = Blueprint('gallery', __name__, url_prefix='/gallery')

@bp.route('/')
def index():
    # TODO: introduce service layer between app (frontend) and models.
    s = Session()
    res = s.query(Item)
    logger.error(res.count())

    return render_template('gallery/index.html')

