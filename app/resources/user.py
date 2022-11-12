from flask.views import MethodView
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from app.models.user import UserModel
from app.schemas import UserLoginSchema, UserSchema

user_blueprint = Blueprint("user", __name__, description="Operations for users.")


@user_blueprint.route("/register")
class UserRegister(MethodView):
    @user_blueprint.arguments(UserSchema)
    def post(self, user_data):
        exist_user = UserModel.find_by_email(user_data["email"])

        if exist_user:
            abort(409, message="A user with that email already exists.")

        new_user = UserModel(
            name=user_data["name"],
            email=user_data["email"],
            role=user_data["role"] if "role" in user_data else None,
            password=generate_password_hash(user_data["password"]),
        )

        try:
            new_user.save()

            tokens = new_user.create_tokens()

            return tokens
        except SQLAlchemyError:
            abort(
                500,
                message="Something wrong happened when registering new user. Please try again.",
            )


@user_blueprint.route("/login")
class UserLogin(MethodView):
    @user_blueprint.arguments(UserLoginSchema)
    def post(self, user_data):
        user = UserModel.find_by_email(user_data["email"])

        if user:
            is_valid_password = check_password_hash(
                user.password, user_data["password"]
            )

            if is_valid_password:
                tokens = user.create_tokens()

                return tokens

        abort(401, message="Invalid email or password. Please try again.")
