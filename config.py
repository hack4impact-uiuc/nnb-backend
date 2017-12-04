import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:

    SECRET_KEY = 'testkey'

    POSTGRES = {
        'user': 'nbb',
        'pw': 'password',
        'db': 'nbb_db',
        'host': 'localhost',
        'port': '5432',
    }

    # SQLALCHEMY_DATABASE_URI = 'postgresql://nbb:password@127.0.0.1:5432/nbb_db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://nbb:password@127.0.0.1:5432/nbb_db'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'default': DevelopmentConfig,
    'prod': ProductionConfig
}
