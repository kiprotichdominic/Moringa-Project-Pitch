from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=6, max=15)])
    confirm_password = PasswordField(
        "Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")
    
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=6, max=15)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")