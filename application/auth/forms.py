from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    """Login form for users"""
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    """Register form for potential new users"""
    name = StringField("Name", [validators.InputRequired()])
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired(),
                                          validators.Length(min=5,
                                          message='Too short password'),
                                          validators.EqualTo('passwordAgain',
                                          message='Passwords must match')])
    passwordAgain = PasswordField("Password again",
                                  [validators.InputRequired()])

    class Meta:
        csrf = False
