# -*- coding: utf-8 -*-
"""Database resource."""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.services import import_models


class Database(object):
    def __init__(self, app=None):
        self.engine = None
        self.metadata = None
        self.session = None
        self.Base = None
        if app:
            self.setup_resource(app.config['SQLALCHEMY_DATABASE_URI'])
            self.init_app(app)

    def setup_resource(self, uri):
        self.engine = create_engine(uri, convert_unicode=True)
        self.metadata = MetaData(bind=self.engine)
        self.session = scoped_session(sessionmaker(autocommit=False,
                                                   autoflush=False,
                                                   bind=self.engine))
        self.Base = declarative_base(metadata=self.metadata)
        self.Base.query = self.session.query_property()
        import_models()

    def init_app(self, app):
        self.setup_resource(app.config['SQLALCHEMY_DATABASE_URI'])

        @app.teardown_appcontext
        def shutdown_session(exception=None):
            self.session.remove()
