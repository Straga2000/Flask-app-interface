from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from  wtforms.validators import DataRequired, Length, Email, EqualTo

MIN_LENGTH = 2
MAX_LENGTH = 20

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = MIN_LENGTH, max = MAX_LENGTH)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')
