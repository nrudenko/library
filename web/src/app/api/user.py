# -*- coding: utf-8 -*-
"""Library api endpoints."""
from flask.blueprints import Blueprint

user_bp = Blueprint('auth', __name__, url_prefix='/api')


@user_bp.route('/')
def create():
    return 'new_token'


@user_bp.route('/login')
def login():
    return 'old_token'


@user_bp.route('/logout')
def logout():
    return 'success'
