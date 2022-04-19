from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField("Имя пользователя", validators=[DataRequired()])
    email = EmailField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password_again = PasswordField("Повторите пароль", validators=[DataRequired()])
    submit = SubmitField("Войти")


class LoginForm(FlaskForm):
    email = EmailField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class EditForm(FlaskForm):
    name = StringField("Имя пользователя")
    email = EmailField("Почта")
    old_password = PasswordField("Старый пароль")
    new_password = PasswordField("Новый пароль")
    new_password_again = PasswordField("Новый пароль ещё раз")
    submit = SubmitField("Подтвердить изменения")
