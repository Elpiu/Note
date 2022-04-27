from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, Form, TextAreaField, PasswordField, BooleanField


class MyForm(Form):
    name    = StringField('Full Name', 
        [validators.DataRequired(), 
        validators.length(max=10)])
    address = TextAreaField('Mailing Address'
        , [validators.optional(), 
        validators.length(max=200)])


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])







