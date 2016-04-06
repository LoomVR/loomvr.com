import os
from flask import Flask, render_template,g, redirect, url_for, flash, jsonify
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import (LoginManager, login_user, logout_user, login_required, current_user)

import forms
import models

app = Flask(__name__)

app.secret_key = "wnfouwui73h7c23b8e8b78bsuiac22"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user

@app.route("/", methods=("GET", "POST"))
def index():
    form = forms.emailList()
    if form.validate_on_submit():
        print(form.email.data)
        print("thanks for your email")
        return render_template("index.html", emailForm = form, thanks ="Thanks!")
    return render_template("index.html", emailForm = form, thanks="Submit")

@app.route("/login", methods=("GET", "POST"))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            loom_user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Email is incorrect. If you havent registered before, <a href='/register'>Go here!</a>", "error")
        else:
            if check_password_hash(loom_user.password, form.password.data):
                login_user(loom_user) # could make an extra field remember me as a boolean
                flash("Logged in", "success")
                return redirect(url_for('index'))
            else:
                flash("Password doesnt match our records", "error")

    return render_template("login.html", form=form)

@app.route("/logout", methods=("GET", "POST"))
def logout():
    logout_user()
    flash("See you soon!", "success")
    return redirect(url_for('index'))

@app.route("/register", methods=("GET", "POST"))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        models.User.create_user(form.username.data,form.firstname.data,
                                            form.lastname.data,form.email.data, form.password.data)
        new_loomer = models.User.select().where(models.User.email ==form.email.data).get()
        login_user(new_loomer)
        return redirect(url_for("index"))
        # return "nice register form submission <a href="">Go Home</a>"
    return render_template("register.html", form=form)

@app.route("/preorder")
def preorder():
    form = forms.preorderForm()
    if form.validate_on_submit():
        #send them an email in the future
        pass
    return render_template("order.html")

@app.route("/blog")
def blog():
    return "Blog coming in the future"

if __name__ == "__main__":
    models.initialize()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
