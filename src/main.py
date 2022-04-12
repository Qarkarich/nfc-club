from flask import Flask, render_template
from flask_login import LoginManager, login_user, logout_user
from data import db_sessions

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwaszxer"
login_manager = LoginManager()


@app.route("/")
def index():
    return "Hello, world!"


def main():
    db_sessions.global_init("db/main")
    app.run(host="127.0.0.1", port="8080")


if __name__ == "__main__":
    main()
