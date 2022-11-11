from flask.views import MethodView
from flask_smorest import Blueprint

user_blueprint = Blueprint("user", __name__, description="Operations for users.")


@user_blueprint.route("/users")
class Users(MethodView):
    def get(self):
        pass
