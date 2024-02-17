from os import environ, path


class Config:
    FLASK_ENV = environ.get('FLASK_ENV')
    DEBUG = True if FLASK_ENV == 'development' else False
    TESTING = True if FLASK_ENV == 'development' else False

    # SECRET_KEY = environ.get('SECRET_KEY')
    SECRET_KEY = 'dev'
    STATIC_FORLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
