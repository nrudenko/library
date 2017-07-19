# -*- coding: utf-8 -*-


class Api(object):
    def __init__(self, app, blueprints):
        for b in blueprints:
            app.register_blueprint(b)
