from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".flaskenv"))


class Config:
    PROPAGATE_EXCEPTIONS = True
    API_TITLE = "Local store RestAPI"
    API_VERSION = "v1"


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get("PROD_DATABASE_URI")


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get("DEV_DATABASE_URI")
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_SWAGGER_UI_PATH = "/"
    OPENAPI_SWAGGER_UI_URL = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
    OPENAPI_URL_PREFIX = "/"
    SQLALCHEMY_DATABASE_URI = "sqlite:///local-store.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
