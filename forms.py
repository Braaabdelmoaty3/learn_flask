from flask_wtf import FlaskForm
from wtforms import stringfeild, PasswordField
from wtforms.validators import data_required, length, email,EqualTo

class RegestrationForm():
    """
    1. put a feild for username 
    2. put some "validators" for that feild (the feild not empty,
        the number of character less and more determend number ) 
    """

    username = stringfeild('username',
                           validators=[data_required(), length(min=2, max=25)])
    email = stringfeild('Email',
                        validators=[data_required(), email()])
    password = PasswordField('passward',validators=[data_required()])
    comferm_password = PasswordField('comferm passward',validators=[data_required(), EqualTo('passward')])
