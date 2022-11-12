from flask.views import MethodView
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from app.blocklist import BLOCKLIST
from app.models.user import UserModel
from app.schemas import (
    BaseUserSchema,
    UserLoginSchema,
    UserPasswordUpdateSchema,
    UserSchema,
    UserUpdateSchema,
)

auth_blueprint = Blueprint(
    "auth", __name__, description="Operations for authentication."
)


@auth_blueprint.route("/register")
class UserRegister(MethodView):
    """
    Register new user API endpoint
    """

    @auth_blueprint.arguments(UserSchema)
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


@auth_blueprint.route("/user")
class UserUpdate(MethodView):
    """
    Update user API endpoint
    """

    @jwt_required()
    @auth_blueprint.arguments(UserUpdateSchema)
    def put(self, user_data):
        current_user = UserModel.get_current_user()

        if current_user:
            if "email" in user_data and user_data["email"] is not current_user.email:
                exist_user_with_provided_email = UserModel.find_by_email(
                    user_data["email"]
                )

                if exist_user_with_provided_email:
                    abort(400, message="This email address is already exists.")

            try:
                current_user.update(
                    email=user_data["email"] if "email" in user_data else None,
                    role=user_data["role"] if "role" in user_data else None,
                    name=user_data["name"] if "name" in user_data else None,
                )

                return {"message": "Successfully updated user."}
            except SQLAlchemyError:
                abort(
                    500,
                    message="Something wrong happened when updating user data. Please try again.",
                )


@auth_blueprint.route("/login")
class UserLogin(MethodView):
    """
    Login API endpoint
    """

    @auth_blueprint.arguments(UserLoginSchema)
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


@auth_blueprint.route("/logout")
class UserLogout(MethodView):
    """
    Logout API endpoint
    """

    @jwt_required()
    def post(self):
        jti = get_jwt().get("jti")

        BLOCKLIST.add(jti)

        return {"message": "Succesfully logged out."}


@auth_blueprint.route("/reset-password")
class UserResetPassword(MethodView):
    """
    Reset password API endpoint
    """

    @jwt_required()
    @auth_blueprint.arguments(UserPasswordUpdateSchema)
    def post(self, user_data):
        user = UserModel.get_current_user()

        is_valid_password = check_password_hash(
            user.password, user_data["current_password"]
        )

        if is_valid_password:
            try:
                user.update(
                    password=generate_password_hash(user_data["new_password"]),
                )

                return {"message": "New password successfully updated."}
            except SQLAlchemyError:
                abort(
                    500,
                    message="Something wrong happened when registering new user. Please try again.",
                )

        abort(401, message="You provided a wrong current password")


@auth_blueprint.route("/user-info")
class UserInfo(MethodView):
    """
    Get current logged in user info API endpoint
    """

    @jwt_required()
    @auth_blueprint.response(200, BaseUserSchema)
    def get(self):
        user = UserModel.get_current_user()

        if user:
            return user

        abort(400, message="No user data found.")


@auth_blueprint.route("/refresh")
class UserRefresh(MethodView):
    """
    Refresh token API endpoint
    """

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()

        new_token = create_access_token(identity=current_user, fresh=False)

        return {"access_token": new_token}
