from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,EqualTo,ValidationError

from models import User


 

class RegistrationForm(FlaskForm):
    """Registration form """

    username = StringField('username_label', validators=[InputRequired(message="Username Required"),
    Length(min=4,max=25, message="username must be  between 4 characters and 25 characters")])
    password = PasswordField('password_label',validators=[InputRequired(message="Password Required"),
    Length(min=4,max=25, message="password must be  between 4 characters and 25 characters")])
    confirm_pswd = PasswordField('confirm_pswd_label', validators=[InputRequired(message="Password Required"),EqualTo("password",message="password must match")])
    submit_button = SubmitField('create')

    def validate_username(self,username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already in use.Select a different username")


