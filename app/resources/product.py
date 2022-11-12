from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from app.models.product import ProductModel
from app.schemas import ProductSchema, ProductSearchSchema, ProductUpdateSchema

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

    @product_blueprint.arguments(ProductUpdateSchema)
    @product_blueprint.response(201, ProductSchema(exclude=["comments"]))
    def put(self, product_data, product_id):
        product = ProductModel.find_by_id(product_id)

        if product:
            try:
                product.update(
                    name=product_data["name"] if "name" in product_data else None,
                    description=product_data["description"]
                    if "description" in product_data
                    else None,
                    price=product_data["price"] if "price" in product_data else None,
                )

                return product
            except SQLAlchemyError:
                abort(
                    500,
                    message="Something wrong happened when updating product. Please try again.",
                )
        else:
            abort(404, message="Cannot find product with provided id.")

    def delete(self, product_id):
        product = ProductModel.find_by_id(product_id)

        if product:
            try:
                product.delete()

                return {"message": "Product successfully deleted."}
            except SQLAlchemyError:
                abort(
                    500,
                    message="Something wrong happened when deleting product. Please try again.",
                )
        else:
            abort(404, message=NO_PRODUCT_FOUND_MESSAGE)


@product_blueprint.route("/product")
class ProductList(MethodView):
    @product_blueprint.arguments(ProductSearchSchema)
    @product_blueprint.response(200, ProductSchema(many=True))
    def get(self, product_data):
        products = ProductModel.search_product(
            name=product_data["name"] if "name" in product_data else None,
        )

        if products:
            return products
        else:
            abort(404, message=NO_PRODUCT_FOUND_MESSAGE)
