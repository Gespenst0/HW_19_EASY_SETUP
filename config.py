class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET = '249y823r9v8238r9u'
    JWT_ALGO = 'HS256'
