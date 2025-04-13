from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError

def username_validator(form, field):
    if field.data.startswith("test"):
        raise ValidationError("用户名不能以test开头")


class LoginForm(FlaskForm):
    username = StringField('用户名', description="用户名")
    password = PasswordField('密码', description="密码")
    submit = SubmitField('提交')


class RegisterForm(FlaskForm):
    username = StringField('用户名', description="用户名", validators=[username_validator])
    password = PasswordField('密码', description="密码", validators=[DataRequired("请输入密码")])
    submit = SubmitField('注册')

    def validate_username(self, filed):
        if filed.data.startswith("admin"):
            raise ValidationError("用户名不能以admin开头")
