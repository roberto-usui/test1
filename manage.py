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
    properties = [Property(price=10, rent=2),
                  Property(price=12, rent=3),
                  Property(price=50, rent=20),
                  Property(price=50, rent=21),
                  Property(price=40, rent=15),
                  Property(price=100, rent=66),
                  Property(price=150, rent=66),
                  Property(price=200, rent=90),
                  Property(price=200, rent=91),
                  Property(price=250, rent=95),
                  Property(price=270, rent=100),
                  Property(price=300, rent=120),
                  Property(price=500, rent=200),
                  Property(price=1000, rent=300),
                  Property(price=2000, rent=600),
                  Property(price=4000, rent=1200),
                  Property(price=4100, rent=1250),
                  Property(price=4200, rent=1300),
                  Property(price=4300, rent=1350),
                  Property(price=4400, rent=1400)
                ]
    table = Table(name='default', properties=properties)
    db.session.add(table)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
