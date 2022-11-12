from app.database import db


class CommentModel(db.Model):  # type: ignore
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String(200), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    product = db.relationship("ProductModel", back_populates="comments")
    user = db.relationship("UserModel", back_populates="comments")

    @classmethod
    def find_by_user_and_product(cls, user_id: int, product_id) -> "CommentModel":
        return cls.query.filter_by(user_id=user_id, product_id=product_id).first()

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()
