from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from app.models.product import ProductModel
from app.schemas import ProductSchema, ProductUpdateSchema

NO_PRODUCT_FOUND_MESSAGE = "No product found."

product_blueprint = Blueprint(
    "product", __name__, description="Operations for product."
)


@product_blueprint.route("/product/<int:product_id>")
class Product(MethodView):
    @product_blueprint.response(200, ProductSchema)
    def get(self, product_id):

        product = ProductModel.find_by_id(product_id)

        if product:
            return product
        else:
            abort(404, message=NO_PRODUCT_FOUND_MESSAGE)
