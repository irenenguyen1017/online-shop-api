from bleach import clean
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from app.models import CommentModel, UserModel
from app.schemas import CommentSchema

comment_blueprint = Blueprint(
    "comment", __name__, description="Operations for comments."
)


@comment_blueprint.route("/comment")
class CommentList(MethodView):
    @comment_blueprint.arguments(CommentSchema)
    @jwt_required()
    def post(self, comment_data):
        current_user = UserModel.get_current_user()

        if current_user:
            exist_comment = CommentModel.find_by_user_and_product(
                user_id=current_user.id, product_id=comment_data["product_id"]
            )

            if exist_comment:
                abort(
                    403,
                    message="You already commented on this product.",
                )
            else:
                comment = CommentModel(
                    user_id=current_user.id,
                    product_id=comment_data["product_id"],
                    content=clean(comment_data["content"]),
                )

                try:
                    comment.save()

                    return {"message": "New comment added successfully."}
                except SQLAlchemyError:
                    abort(
                        500,
                        message="Something wrong happened when registering new user. Please try again.",
                    )
        else:
            abort(403, message="Not authorized.")
