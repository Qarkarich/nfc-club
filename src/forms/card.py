from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


class CardForm(FlaskForm):
    name = StringField("Название карты", validators=[DataRequired()])
    title = StringField("Заголовок карты")
    link = StringField("Сокращение ссылки")
    main = StringField("Основной текст")
    description = StringField("Дополнительный текст")
    phone = StringField("Номер телефона")
    mail = StringField("Почта")
    site_vk = StringField("Ссылка на ВКонтакте")
    site_instagram = StringField("Ссылка на Instargram")
    site_telegram = StringField("Ссылка на Telegram")
    site_discord = StringField("Ссылка на Discord")

    submit = SubmitField("Сохранить")
