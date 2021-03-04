import os
import sys
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config:
    APP_NAME = os.environ.get('APP_NAME', 'Tabletop-Game')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    print('sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL',
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')


config = {
    'default': DevelopmentConfig
}
