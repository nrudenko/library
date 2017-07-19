# -*- coding: utf-8 -*-
"""Books endpoints."""
import flask
from flask.blueprints import Blueprint

from app import booksController


book_bp = Blueprint('books', __name__, url_prefix='/api/book')


@book_bp.route('', methods=['GET'])
def create():
    name = flask.request.args.get('name', None)
    if not name:
        return flask.jsonify({'error': 'empty name parameter', 'code': '400'}), 400
    books = booksController.get_second_book_with_same_price(name)
    return flask.jsonify(books=[dict(row) for row in books]
                         )
