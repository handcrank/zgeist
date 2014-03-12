# -*- coding: utf-8 -*-
# vim: expandtab shiftwidth=4 softtabstop=4
"""
    zgeist.models.item
    ~~~~~~~~~~~~~~~~~~

    item model
"""

from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean

from base import Base

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)

