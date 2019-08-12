from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    """Login form for users"""
    username = StringField("Username", render_kw={"placeholder": "Username"})
    password = PasswordField("Password", render_kw={"placeholder": "Password"})

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    """Register form for potential new users"""
    name = StringField("Name", [validators.Length(min=5, max=20)],
                       render_kw={"placeholder": "Name"})
    username = StringField("Username", [validators.Length(min=2, max=20)],
                           render_kw={"placeholder": "Username"})
    password = PasswordField("Password", [validators.Length(min=5, max=30)],
                             render_kw={"placeholder": "Password"})
    passwordAgain = PasswordField("Password again",
                                  [validators.Length(min=5, max=30)],
                                  render_kw={"placeholder": "Password again"})

    class Meta:
        csrf = False
