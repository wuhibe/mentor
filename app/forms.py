from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from models.student import Student


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    fname = StringField('First name', validators=[DataRequired()])
    lname = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    github = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(),
                              EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        s = Student.query.filter_by(username=username.data).first()
        if s is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        s = Student.query.filter_by(email=email.data).first()
        if s is not None:
            raise ValidationError('Please use a different email address.')
