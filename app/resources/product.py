from flask.views import MethodView
from flask_smorest import Blueprint

product_blueprint = Blueprint(
    "product", __name__, description="Operations for product."
)


@product_blueprint.route("/products")
class Products(MethodView):
    def get(self):
        pass
