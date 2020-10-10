from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    # RegistrationForm(FlaskForm) -znaci da nasledjuje FlaskForm
    # sada kreiramo polja u formi
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sing up')

    # ovo je motad koja vrsi validacu konkretnog polja username koje ne sme biti isto
    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already exist! Please chose a different!')

    # a ovo je metoda za validaciju mejla
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already exist! Please chose a different!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remeber = BooleanField('Remember me')
    submit = SubmitField('Login')


class UpdateAccount(FlaskForm):
    # UpdateAccount(FlaskForm) -znaci da nasledjuje FlaskForm
    # sada kreiramo polja u formi
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    # ovo je motad koja vrsi validacu konkretnog polja username koje ne sme biti isto
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    # a ovo je metoda za validaciju mejla
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Reqest Reset Passowrd')

    # a ovo je metoda za validaciju mejla, tj ako ne postoji mejl ne mozemo da posaljemo obavestenje za restart sifre
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPaswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(' Reset Passowrd')