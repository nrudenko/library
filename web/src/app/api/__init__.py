# -*- coding: utf-8 -*-
"""Library endpoints group."""
from user import user_bp
from book import book_bp

blueprints_list = [
    user_bp,
    book_bp,
]
__all__ = 'blueprints_list'
