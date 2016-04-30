from flask.ext.wtf import Form
from wtforms import (StringField, PasswordField, TextAreaField, DecimalField,
        RadioField, SelectMultipleField, widgets, FileField, validators, IntegerField)
from wtforms.validators import (InputRequired, Regexp, ValidationError, Email, Length, EqualTo)


class RegisterForm(Form):

    username = StringField('Username', validators=
                [InputRequired(), Regexp(r'^[a-zA-Z0-9_]+$', message=(
                                            'Username should be one word, letters, numbers and underscores only!'))])


    firstname = StringField('First Name', validators=
                [InputRequired(), Regexp(r'^[A-Z][a-z_]*$', message=(
                                            'Please capitalize the first letter'))])
    lastname = StringField('Last Name', validators=
                [InputRequired(), Regexp(r'^[A-Z][a-z_]*$', message=(
                                            'Please capitalize the first letter'))])
    email = StringField('Email', validators=[InputRequired(), Email()]) # make sure to add validators

    password = PasswordField('Password', validators=[InputRequired(), Length(min=5),
    EqualTo('password_confirm', message="Passwords must match")])

    password_confirm = PasswordField('Confirm Password', validators=[InputRequired()])


class LoginForm(Form):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class preorderForm(Form):
    email= StringField("Email you want us to send access code to", validators=[InputRequired()])
    #more work needed

class contactForm(Form):
    message= TextAreaField()

class emailList(Form):
    email= StringField("Join our mailing list", validators=[InputRequired(), Email()])
