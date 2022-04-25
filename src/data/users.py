import datetime as dt

import sqlalchemy as sa
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String, unique=True)
    name = sa.Column(sa.String, nullable=True)
    hashed_password = sa.Column(sa.String)
    created_data = sa.Column(sa.DateTime, default=dt.datetime.now)

    cards = orm.relation("Card", back_populates="user")

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def is_get_card(self, card):
        return card.id in [i.id for i in self.cards]
