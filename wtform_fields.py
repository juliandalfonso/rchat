from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    """Registration form"""
    username = StringField('username_label', 
    validators=[InputRequired(message="Nombre de usuario requerido"), 
    Length(min=4, max=25, 
    message="El nombre de usuario debe tener entre 4 a 25 caracteres")])

    password = PasswordField('password_label',
    validators=[InputRequired(message="La contraseña es requerida"), 
    Length(min=4, max=25, 
    message="La contraseña debe tener entre 4 a 25 caracteres")])

    confirm_pswd = PasswordField('confirm_pswd_label',
    validators=[InputRequired(message="La contraseña es requerida"), 
    EqualTo('password', message="Las contraseñas deben coincidir.")])

    submit_button = SubmitField('Create')
    