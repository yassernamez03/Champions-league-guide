from flask import Flask, redirect,render_template, request, session, url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField
from wtforms.validators import DataRequired,InputRequired,EqualTo


class LoginForm(FlaskForm):
    name = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')
class SignupForm(FlaskForm):
    name = StringField('UserName',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('New Password', [DataRequired()])
    confirm  = PasswordField('Repeat Password',[DataRequired()])
    submit = SubmitField('SignUp')