# -*- coding: utf-8 -*-
"""Library application entry point."""
import os

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from resources import Database
from resources import Api
from api import blueprints_list

db = Database()


def create_app():
    """Create app factory method."""
    app = Flask(__name__)
    app.config.from_pyfile(os.environ['LIBRARY_CONF'])

    init_app(app)
    init_admin_panel(app)

    return app


def init_admin_panel(app):
    admin = Admin(app, name='library', url='/admin', template_mode='bootstrap3')
    from app.services.users.models import User
    from app.services.books.models import Book
    from app.services.books.models import Author
    from app.services.rents.models import Rent

    admin.add_view(ModelView(Book, db.session))
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Author, db.session))
    admin.add_view(ModelView(Rent, db.session))


def init_app(app):
    """Init plugins and third party resources."""
    db.init_app(app)
    Api(app, blueprints_list)
