"""
@Time   : 2026/8/4  00:11
@AUTHOR : urchiola@163.com
@file   : http.py
"""
from flask import Flask
from internal.router.router import Router
from config import Config

class Http(Flask):
    """Http 服务引擎"""

    def __init__(self, *args, conf:Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        ### 注册应用路由
        router.register_router(self)  ## self 恰好是 Flask

        # 通过对象方式将conf 加载到当前应用中
        # 这里通过调用父类(flesk)的配置信息
        self.config.from_object(conf)