from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,EqualTo

from models import User


 
   # check credentials  are valid 

    user_object = User.query.filter_by(username=username.data).first()
    if  user_object in None :
        raise ValidationError('username or password is  invalid ')
    elif password_entered != user_object.password:
        raise ValidationError('Username or password is invalid ')


class RegistrationForm(FlaskForm):
    """Registration form """

    username = StringField('username_label', validators=[InputRequired(message="Username Required"),
    Length(min=4,max=25, message="username must be  between 4 characters and 25 characters")])
    password = PasswordField('password_label',validators=[InputRequired(message="Password Required"),
    Length(min=4,max=25, message="password must be  between 4 characters and 25 characters")])
    confirm_pswd = PasswordField('confirm_pswd_label', validators=[InputRequired(message="Password Required"),EqualTo("password",message="password must match")])
    submit_button = SubmitField('create')
