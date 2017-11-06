
DEBUG = False

SECRET_KEY = 'testkey'

POSTGRES = {
    'user': 'nbb',
    'pw': 'password',
    'db': 'nbb_db',
    'host': 'localhost',
    'port': '5432',
}

SQLALCHEMY_DATABASE_URI = 'postgresql://nbb:password@127.0.0.1:5432/nbb_db'

SQLALCHEMY_TRACK_MODIFICATIONS = False