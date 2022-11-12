from typing import List

from app.database import db


class ProductModel(db.Model):  # type: ignore
    __tablename__ = "products"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    description = db.Column(db.String(100), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    comments = db.relationship("CommentModel", back_populates="product", lazy="dynamic")

    def __repr__(self):
        return f"ProductModel(name={self.name}, price={self.price}, description={self.description})"

    def update(
        self,
        name: str | None = None,
        description: str | None = None,
        price: float | None = None,
    ) -> None:
        if price and price is not self.price:
            self.password = price
        if description and description is not self.description:
            self.description = description
        if name and name is not self.name:
            self.name = name

        db.session.commit()

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
