from sqlalchemy_utils import EmailType

from app.database import db
from app.typings import Role


class UserModel(db.Model):  # type: ignore
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Enum(Role), nullable=False, default=Role.user)
    name = db.Column(db.Unicode(50), nullable=False)
    email = db.Column(EmailType, unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    comments = db.relationship("CommentModel", back_populates="user", lazy="dynamic")

    def __repr__(self):
        return f"UserModal(name={self.name}, email={self.email}, role={self.role})"

    def is_admin(self):
        return self.role == Role.admin

    def update(
        self,
        role: Role | None = None,
        password: str | None = None,
        email: EmailType | None = None,
        name: str | None = None,
    ) -> None:
        if role and role is not self.role:
            self.role = role
        if password and password is not self.password:
            self.password = password
        if email and email is not self.email:
            self.email = email
        if name and name is not self.name:
            self.name = name

        db.session.commit()

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
