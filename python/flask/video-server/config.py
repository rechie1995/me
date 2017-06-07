import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'dev-data.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'dev_db_repository')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'test-data.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'test_db_repository')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'data.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'procduction' : ProductionConfig,

    'default' : DevelopmentConfig
}