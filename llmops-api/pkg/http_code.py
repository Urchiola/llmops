"""
@Time   : 2026/9/16  22:03
@AUTHOR : urchiola@163.com
@file   : http_code.py
"""
from enum import Enum

class HttpCode(str, Enum):
    """http 基础业务状态码"""
    SUCCESS = "success" # 成功状态
    FAIL="fail" # 失败状态
    NOT_FOUND="not_found" # 未找到
    UNAUTHORIZED="unauthorized" # 未授权
    FORBIDDEN="forbidden" # 无权限
    VALIDATE_ERROR="validate_error"
