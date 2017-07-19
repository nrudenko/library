# -*- coding: utf-8 -*-
from sqlalchemy import text


class BooksController(object):

    def __init__(self, db):
        self.db = db
        super(BooksController, self).__init__()

    def get_second_book_with_same_price(self, name):
        query = "SELECT * FROM book WHERE price = ( " \
                  "SELECT book.price " \
                  "FROM library_user JOIN rent ON rent.library_user_id=library_user.id " \
                  "JOIN book ON rent.book_id = book.id " \
                  "WHERE library_user.first_name ||' '||library_user.last_name  LIKE :name " \
                  "ORDER BY rent.start_date LIMIT 1 OFFSET 1);"
        return self.db.engine.execute(text(query), {'name': '%{0}%'.format(name)}).fetchall()
