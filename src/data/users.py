from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
import sqlalchemy as sa
import datetime as dt


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    hashed_password = sa.Column(sa.String)
    modified_data = sa.Column(sa.DateTime, default=dt.datetime.now())

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
