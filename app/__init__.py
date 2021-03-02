import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config as Config

basedir = os.path.abspath(os.path.dirname(__file__))

__version__ = '0.0.1'

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config['default'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    Config['default'].init_app(app)
    db.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.game import game as game_blueprint
    app.register_blueprint(game_blueprint)

    return app
