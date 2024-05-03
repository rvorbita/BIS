from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators, NumberField, SubmitField



class EntryForm(FlaskForm):

    fname = StringField('FirstName', validators=[validators.Length(min=4, max=25), validators.DataRequired()])
    lname = StringField('LastName', validators=[validators.Length(min=4, max=25), validators.DataRequired()])
    mname = StringField('MiddleName', validators=[validators.Length(min=4, max=25), validators.DataRequired()])
    age = NumberField('Age', validators=[validators.DataRequired()])
    address = StringField('Address', validators=[validators.DataRequired()])
    submit = SubmitField('Submit')




class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[validators.Length(min=4, max=25)])
    email = StringField('Email Address', validators=[validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

