# -*- coding: utf-8 -*-
"""Library manage script."""

import unittest

from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager

from app import create_app, db

app_instance = create_app()
migrate = Migrate(app_instance, db)
manager = Manager(app_instance)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    from colour_runner.runner import ColourTextTestRunner

    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = ColourTextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
