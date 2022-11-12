from flask import Flask
from flask_cors import CORS
from flask_smorest import Api

from app.database import db
from app.resources.comment import comment_blueprint
from app.resources.product import product_blueprint
from app.resources.user import user_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("app.config.DevConfig")
    db.init_app(app)
    api = Api(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    api.register_blueprint(comment_blueprint)
    api.register_blueprint(product_blueprint)
    api.register_blueprint(user_blueprint)

    return app
