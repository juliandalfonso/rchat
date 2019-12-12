from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from models import User


def invalid_credentials(form, field):
    """Username and password checker"""

    username_entered = form.username.data
    password_entered = field.data

    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError(
            "Nombre de usuario o contraseña incorrecta")
    elif password_entered != user_object.password:
        raise ValidationError("Nombre de usuario o contraseña incorrecta")


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

    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError(
                "Nombre de usuario existente, porfavor selecciona otro")


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('username_label', validators=[
                           InputRequired(message="Nombre de usuario requerido")])
    password = PasswordField('password_label', validators=[
        InputRequired(message="La contraseña es requerida"), invalid_credentials])
    submit_button = SubmitField('Create')
