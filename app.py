import os
from flask import Flask, render_template,g, redirect
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import (LoginManager, login_user, logout_user, login_required, current_user)

import forms

app = Flask(__name__)

app.secret_key = "wnfouwui73h7c23b8e8b78bsuiac22"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=("GET", "POST"))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        return "awesome login bro, welocme to loom <a href="">Go Home</a>"
    return render_template("login.html", form=form)

@app.route("/register", methods=("GET", "POST"))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        return "nice register form submission <a href="">Go Home</a>"
    return render_template("register.html", form=form)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
