"""
@Time   : 2026/9/15  23:13
@AUTHOR : urchiola@163.com
@file   : app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口请求验证"""
    query = StringField("query", validators=[
        DataRequired(
            message="用户提问是必填的"
        ),
        Length(
            min=3,
            max=1000,
            message="用户提问最小长度为3，最大长度为1000"
        )
    ])