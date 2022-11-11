from flask.views import MethodView
from flask_smorest import Blueprint

comment_blueprint = Blueprint(
    "comment", __name__, description="Operations for comment."
)


@comment_blueprint.route("/comments")
class Comments(MethodView):
    def get(self):
        pass
