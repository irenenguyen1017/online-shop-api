from marshmallow import Schema, ValidationError, fields, validates_schema

from app.typings import Role


class BaseProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str(required=True)


class BaseCommentSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)


class BaseUserSchema(Schema):
    id = fields.Int(dump_only=True)
    role = fields.Enum(Role)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)


class UserUpdateSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    role = fields.Enum(Role)


class UserPasswordUpdateSchema(Schema):
    current_password = fields.Str(required=True)
    new_password = fields.Str(required=True)
    new_confirm_password = fields.Str(required=True)

    @validates_schema
    def validate_password(self, data, **kwargs):
        if data["new_password"] != data["new_confirm_password"]:
            raise ValidationError("Confirm password is not matched.")


class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class ProductUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    description = fields.Str()


class ProductSearchSchema(Schema):
    name = fields.Str()


class CommentSchema(BaseCommentSchema):
    product_id = fields.Int(required=True, load_only=True)
    product = fields.Nested(BaseProductSchema(), dump_only=True)
    user = fields.Nested(BaseUserSchema(only=["name"]), dump_only=True)


class ProductSchema(BaseProductSchema):
    comments = fields.List(
        fields.Nested(CommentSchema(exclude=["product"])), dump_only=True
    )


class UserSchema(BaseUserSchema):
    comments = fields.List(fields.Nested(CommentSchema()), dump_only=True)
