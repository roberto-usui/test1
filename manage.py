#!/usr/bin/env python
import os
import subprocess

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app, db
from app.models import Table, Player, Property
from config import Config

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def setup_dev():
    """Runs the set-up needed for local development."""
    setup_general()


def setup_general():
    """Runs the set-up needed for both local development and production.
       Also sets up first admin user."""
    Player.insert_players()
    properties = [Property(price=10, rent=4),
                  Property(price=12, rent=3),
                  Property(price=50, rent=20),
                  Property(price=50, rent=21),
                  Property(price=40, rent=12),
                  Property(price=100, rent=66),
                  Property(price=200, rent=150),
                  Property(price=200, rent=150),
                  Property(price=200, rent=150),
                  Property(price=200, rent=150),
                  Property(price=200, rent=150),
                  Property(price=200, rent=150),
                  Property(price=200, rent=150)
                ]
    table = Table(name='default', properties=properties)
    db.session.add(table)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
