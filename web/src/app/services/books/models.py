# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy import Float
from sqlalchemy.orm import relationship

from app import db


class Book(db.Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String(13), nullable=False)
    name = Column(Text, nullable=False)
    short_description = Column(Text, nullable=False)
    release_date = Column(Date, nullable=False)
    price = Column(Float, nullable=False, default=0)
    created_at = Column(Date, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        try:
            return '{name} {price}$'.format(**self.__dict__)
        except:
            return self.__repr__()


class Author(db.Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=False)


class AuthorBook(db.Base):
    __tablename__ = 'author_book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(ForeignKey(u'author.id'), nullable=False)
    book_id = Column(ForeignKey(u'book.id'), nullable=False)

    author = relationship(u'Author')
    book = relationship(u'Book')

    def __repr__(self):
        return '{value}'.format(**self.__dict__)


class Review(db.Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rate = Column(Integer, nullable=False)
    text = Column(Text)
    library_user_id = Column(ForeignKey(u'library_user.id'), nullable=False)
    book_id = Column(ForeignKey(u'book.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)

    book = relationship(u'Book')
    library_user = relationship(u'LibraryUser')
