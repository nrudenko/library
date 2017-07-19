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
    owner_id = Column(ForeignKey(u'library_user.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    library_user_id = Column(ForeignKey(u'library_user.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.datetime.utcnow)

    owner = relationship(u'LibraryUser', primaryjoin='Following.owner_id == LibraryUser.id')
    library_user = relationship(u'LibraryUser', primaryjoin='Following.library_user_id == LibraryUser.id')

