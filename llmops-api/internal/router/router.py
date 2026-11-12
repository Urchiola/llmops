"""
@Time   : 2026/8/3  23:49
@AUTHOR : urchiola@163.com
@file   : router.py
"""

from dataclasses import dataclass

"""自动生成构造函数"""

from flask import Flask, Blueprint
from injector import inject

from handler import AppHandler, IndexHandler


@inject
@dataclass
class Router:
    """"路由"""
    app_handler: AppHandler  ### @inject + dataclass 会自动注入
    index_handler: IndexHandler

    def register_router(self, app: Flask):
        """注册路由"""

        """1.创建一个蓝图"""
        bp = Blueprint('llmops', __name__, url_prefix='')

        """ 2.将url 对应的控制器方法做绑定 """
        bp.add_url_rule('/', view_func=self.index_handler.print)
        bp.add_url_rule('/app/completion', methods=['POST'], view_func=self.app_handler.completion)
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)

        """3.在应用上注册蓝图"""
        app.register_blueprint(bp)
