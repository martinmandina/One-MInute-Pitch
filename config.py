import os

class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martinmandina:alicewambui@localhost/pitch'

class ProdConfig(Config):
    pass
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martinmandina:alicewambui@localhost/pitch'
class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martinmandina:alicewambui@localhost/pitch'

config_options = {
'development':DevConfig,
'production':ProdConfig
}

