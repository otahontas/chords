from flask import flash, render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    """View controller for user login"""
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/loginform.html", form=form)

    user = User.query.filter_by(username=form.username.data,
                                password=form.password.data).first()

    if not user:
        form.username.errors.append("Username or password incorrect")
        return render_template("auth/loginform.html", form=form)

    login_user(user)
    flash('You were successfully logged in')
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    """View controller for user logout"""
    flash('You were successfully logged out')
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    """View controller for new user registering"""
    if request.method == "GET":
        return render_template("auth/register.html", form=RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/register.html", form=form)

    taken_username = User.query.filter_by(username=form.username.data).first()
    if taken_username:
        form.username.errors.append("This username is already taken")
        return render_template("auth/register.html", form=form)

    user = User(form.name.data, form.username.data, form.password.data)

    db.session().add(user)
    db.session().commit()

    flash('Your account was succesfully created, please login')
    return redirect(url_for("auth_login"))
