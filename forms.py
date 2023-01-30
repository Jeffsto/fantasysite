from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, PasswordField)
from wtforms.validators impoart InputRequired, Length, Email, EqualTo,

class LoginForm(form):

