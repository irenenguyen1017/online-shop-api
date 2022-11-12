from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from app.blocklist import BLOCKLIST
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

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_loader(jwt_payload):
        return jsonify(
            {"message": "The token has been revoked.", "error": "token_revoked"}, 401
        )

    @jwt.expired_token_loader
    def expired_token_loader_handler(jwt_header, jwt_payload):
        return jsonify(
            {"message": "Expired token provided.", "error": "token_expired"}, 401
        )

    @jwt.invalid_token_loader
    def invalid_token_handler(jwt_payload):
        return jsonify(
            {"message": "Invalid token provided.", "error": "token_invalid"}, 401
        )

    @jwt.unauthorized_loader
    def unauthorized_loader(jwt_payload):
        return jsonify(
            {
                "message": "Request does not contain an access token.",
                "error": "token_expired",
            },
            401,
        )

    @app.before_first_request
    def create_tables():
        db.create_all()

    api.register_blueprint(comment_blueprint)
    api.register_blueprint(product_blueprint)
    api.register_blueprint(user_blueprint)

    return app
