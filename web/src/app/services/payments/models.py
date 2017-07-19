# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Float
from sqlalchemy.orm import relationship

from app import db


class Order(db.Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(u'user.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.datetime.utcnow)
    close_date = Column(Date)

    user = relationship(u'User')


class OrderItem(db.Base):
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Integer, nullable=False)
    amount_to_pay = Column(Float, nullable=False)
    rent_id = Column(ForeignKey(u'rent.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    order_id = Column(ForeignKey(u'order.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)

    order = relationship(u'Order')
    rent = relationship(u'Rent')


class PaymentTransaction(db.Base):
    __tablename__ = 'payment_transaction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(ForeignKey(u'order.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    transaction_hash = Column(String(32), nullable=False)
    is_successful = Column(Boolean, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.datetime.utcnow)

    order = relationship(u'Order')
