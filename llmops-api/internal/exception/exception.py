"""
@Time   : 2026/9/23  22:39
@AUTHOR : urchiola@163.com
@file   : exception.py
"""
from pkg.response import HttpCode
from typing import Any
from dataclasses import field
class CustomException(Exception):
    """基础自定义异常信息"""
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    # def __init__(self, data: dict = None): 