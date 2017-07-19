# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from app import db


class Rent(db.Base):
    __tablename__ = 'rent'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(ForeignKey(u'book.id'), nullable=False)
    library_user_id = Column(ForeignKey(u'library_user.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    close_date = Column(Date)
    created_at = Column(Date, nullable=False, default=datetime.datetime.utcnow)

    book = relationship(u'Book')
    library_user = relationship(u'LibraryUser')
