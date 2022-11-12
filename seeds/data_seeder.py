from flask_bcrypt import generate_password_hash
from flask_seeder import Faker, Seeder, generator
from sqlalchemy.exc import SQLAlchemyError

from app.models import CommentModel, ProductModel, UserModel
from app.typings import Role


class DataSeeder(Seeder):
    def run(self):
        # Clear all the data base before seeding
        try:
            UserModel.query.delete()
            ProductModel.query.delete()
            UserModel.query.delete()
            self.db.session.commit()
        except SQLAlchemyError:
            self.session.rollback()

        admin_user = Faker(
            cls=UserModel,
            init={
                "name": generator.Name(),
                "email": "admin@test.com",
                "role": Role.admin,
                "password": generate_password_hash("123"),
            },
        )

        for admin in admin_user.create(1):
            print("Adding admin: %s" % admin)
            self.db.session.add(admin)

        base_user = Faker(
            cls=UserModel,
            init={
                "name": generator.Name(),
                "email": "user@test.com",
                "role": Role.user,
                "password": generate_password_hash("123"),
            },
        )

        for user in base_user.create(1):
            print("Adding user: %s" % user)
            self.db.session.add(user)

        products = Faker(
            cls=ProductModel,
            init={
                "name": generator.String(pattern=r"abc\d{4}[i-m]{2}[qwerty]xyz"),
                "description": generator.String("Product description"),
                "price": generator.Integer(),
            },
        )

        for product in products.create(5):
            print("Adding product: %s" % product)
            self.db.session.add(product)
