# -*- coding: utf-8 -*-
# vim: expandtab shiftwidth=4 softtabstop=4
"""
    zgeist
    ~~~~~~

    zgeist module
"""

from conf import config
from util import approot
from models.base import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

import logging.config

def _get_session():
    """Returns a scoped session used throughout the app."""
    engine = create_engine(config['database.uri'])
    session_factory = sessionmaker(bind=engine)
    return scoped_session(session_factory)
Session = _get_session()

logging.config.dictConfig(config['logger'])
#('%(asctime)s %(levelname)s %(name)s [%(filename)s:%(lineno)s] %(message)s')

