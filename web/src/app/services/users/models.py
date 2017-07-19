# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column, ForeignKey, Text, Boolean, Date
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app import db


class AuthCredential(db.Base):
    __tablename__ = 'auth_credential'

    id = Column(Integer, primary_key=True, autoincrement=True)
    library_user_id = Column(ForeignKey(u'library_user.id'), nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.datetime.utcnow)

    library_user = relationship(u'LibraryUser')


class LibraryUser(db.Base):
    __tablename__ = 'library_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(Text, nullable=False, unique=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    is_confirmed = Column(Boolean, nullable=False, default=False)
    created_at = Column(Date, nullable=False, default=datetime.datetime.utcnow)
    updated_at = Column(Date)

    def __repr__(self):
        return '{first_name} {last_name} ({email})'.format(**self.__dict__)


class Role(db.Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Integer, nullable=False)
    title = Column(Integer, nullable=False)


class LibraryUserRole(db.Base):
    __tablename__ = 'library_user_role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    library_user_id = Column(ForeignKey(u'library_user.id'), nullable=False)
    role_id = Column(ForeignKey(u'role.id'), nullable=False)

    role = relationship(u'Role')
    library_user = relationship(u'LibraryUser')

