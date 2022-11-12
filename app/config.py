from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".flaskenv"))


class Config:
    PROPAGATE_EXCEPTIONS = True
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_TITLE = "Online store API"
    API_VERSION = "v1"


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get("PROD_DATABASE_URI")


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_SWAGGER_UI_PATH = "/"
    OPENAPI_SWAGGER_UI_URL = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
    OPENAPI_URL_PREFIX = "/"
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")
    JWT_SECRET_KEY = "25432980928529878777477170733653477453"
