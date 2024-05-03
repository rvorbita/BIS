from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators, IntegerField, SubmitField



class EntryForm(FlaskForm):

    fname = StringField('FirstName', validators=[validators.Length(min=4, max=25), validators.DataRequired()])
    lname = StringField('LastName', validators=[validators.Length(min=4, max=25), validators.DataRequired()])
    mname = StringField('MiddleName', validators=[validators.Length(min=4, max=25), validators.DataRequired()])
    age = IntegerField('Age', validators=[validators.Length(min=1,max=99),validators.DataRequired()])
    address = StringField('Address', validators=[validators.DataRequired()])
    submit = SubmitField('Submit')



class LoginForm(FlaskForm):

    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[validators.Length(min=4, max=25)])
    email = StringField('Email Address', validators=[validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

