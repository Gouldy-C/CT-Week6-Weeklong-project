from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class SignInForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class SignUpForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired()])
    email = StringField('Email',
                            validators=[DataRequired()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    password2 = PasswordField('Confirm Password ',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')