import flask_login
from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, logout_user, current_user
from data import db_session
from forms.user import RegisterForm, LoginForm, EditForm
# from forms.card import CardForm
from data.users import User
from data.cards import Card

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwaszxer"
login_manager = LoginManager()


@app.errorhandler(404)
def not_found_error(error):
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("index.html", title="Главная", cards=current_user.cards)
    else:
        return render_template("index_unauth.html", title="Авторизируйтесь или зарегистрируйтесь ")


@app.route("/register", methods=["GET", "POST"])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template("register.html", title="Регистрация",
                                   form=form,
                                   message="Пароли не совпадают")

        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template("register.html", title="Регистрация",
                                   form=form,
                                   message="Данная почта уже кем-то занята")
        if db_sess.query(User).filter(User.name == form.name.data).first():
            return render_template("register.html", title="Регистрация",
                                   form=form,
                                   message="Данное имя уже кем-то занято")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/login")

    return render_template("register.html", title="Регистрация", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template("login.html",
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template("login.html", title="Авторизация", form=form)


@flask_login.login_required
@app.route("/card/<int:card_id>/view")
def card_settings(card_id):
    # if not current_user.is_authenticated:
    #     return redirect("/")

    db_sess = db_session.create_session()
    card = db_sess.query(Card).get(card_id)

    if not card or not current_user.is_get_card(card):
        return redirect("<h1>BAD REQUEST</h1>")

    # form = CardForm()
    # if request.method == "GET":
    #     form.name.data = card.name
    #     form.phone.data = card.phone
    #
    # if form.validate_on_submit():
    #     pass

    return render_template("blocks/card_view.html", title=f"Карта #{card.id}", card=card)


@flask_login.login_required
@app.route("/profile")
def check_profile():
    return render_template("profile_view.html", title=f"Просмотр профиля", user=current_user)


@flask_login.login_required
@app.route("/profile/edit", methods=["GET", "POST"])
def edit_profile():
    form = EditForm()
    if request.method == "GET":
        form.email.data = current_user.email
        form.name.data = current_user.name
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        if user:
            if form.new_password.data != "" or form.old_password.data != "":
                if not user.check_password(form.old_password.data):
                    return render_template("profile_edit.html", title="Редактировать профиль",
                                           form=form, message="Старый пароль введен некорректно")
                if form.new_password.data != form.new_password_again.data:
                    return render_template("profile_edit.html", title="Редактировать профиль",
                                           form=form, message="Введенные пароли не совпадают")
                user.set_password(form.new_password.data)

            user.name = form.name.data
            user.email = form.email.data

            db_sess.commit()
            return redirect("/")
        else:
            return abort(404)

    return render_template("profile_edit.html", title="Редактировать профиль", form=form)


def main():
    db_session.global_init("db/main.sqlite")
    login_manager.init_app(app)
    app.run(host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
