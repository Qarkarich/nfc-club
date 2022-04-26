from .db_session import SqlAlchemyBase
import sqlalchemy as sa
from sqlalchemy import orm
import datetime as dt


class Card(SqlAlchemyBase):
    __tablename__ = "cards"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    owner_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    name = sa.Column(sa.String, nullable=True)
    title = sa.Column(sa.String, nullable=True)
    link = sa.Column(sa.String, nullable=True)
    main = sa.Column(sa.String, nullable=True)
    description = sa.Column(sa.String, nullable=True)
    phone = sa.Column(sa.String, nullable=True)
    mail = sa.Column(sa.String, nullable=True)
    site_vk = sa.Column(sa.String, nullable=True)
    site_instagram = sa.Column(sa.String, nullable=True)
    site_telegram = sa.Column(sa.String, nullable=True)
    site_discord = sa.Column(sa.String, nullable=True)
    created_data = sa.Column(sa.DateTime, default=dt.datetime.now)

    user = orm.relation("User")
