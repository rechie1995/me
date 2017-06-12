# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Required, Length, Regexp, EqualTo, IPAddress
from wtforms import ValidationError
from ..models import User

# 简单的Web表单
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# 定义的表单都需要继承子FlaskForm
class LoginForm(FlaskForm):
    # 域初始化时，第一个参数是设置label属性的
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in', default=False)
    submit = SubmitField('Log In')

class ChoicesForm(FlaskForm):
    status = SelectField('camera choice', validators=[Required()], choices=[('0','bedroom'),
                                                                            ('1','classroom')])
    submit = SubmitField('Choice')

# 定义一个注册表单
class RegistrationForm(FlaskForm):
    username = StringField('User Name', validators=[
        Required(), Length(1, 64), 
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots, or underscores')
    ])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Password must match.')
    ])
    password2 = PasswordField('Confirm password', validators=[
        Required()
    ])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class SettingsForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired()])
    IPAddress = StringField('IP', validators=[IPAddress()])
    Port = StringField('Port', validators=[DataRequired()])
    submit = SubmitField('Set')