"""
@Time   : 2026/9/15  23:34
@AUTHOR : urchiola@163.com
@file   : config.py
"""

class Config:
    def __init__(self):
        #关闭 wtf 的CSRF保护
        self.WTF_CSRF_ENABLED = False