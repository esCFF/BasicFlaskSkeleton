import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '72?43ñ4sdFDsAsjdj243cyoL0o?Ñqp198031417'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

