from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


class CardForm(FlaskForm):
    name = StringField("Название карты", validators=[DataRequired()])
    title = StringField("Заголовок карты")
    description = StringField("Подробная информация карты")
    email = EmailField("Почта")
    phone = StringField("Телефон")
    submit = SubmitField("Сохранить")
