# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy.orm import relationship

from app import db


class Following(db.Base):
    __tablename__ = 'following'

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(ForeignKey(u'user.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    user_id = Column(ForeignKey(u'user.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.datetime.utcnow)

    owner = relationship(u'User', primaryjoin='Following.owner_id == User.id')
    user = relationship(u'User', primaryjoin='Following.user_id == User.id')

