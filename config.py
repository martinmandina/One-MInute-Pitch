import os

class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martinmandina:alicewambui@localhost/pitchy'

class ProdConfig(Config):
    pass
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martinmandina:alicewambui@localhost/pitchy'
class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martinmandina:alicewambui@localhost/pitchy'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig
}

