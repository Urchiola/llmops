"""
@Time   : 2026/8/4  00:15
@AUTHOR : urchiola@163.com
@file   : app.py
"""
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import Http
import dotenv

# 将.env 加载到环境变量中
dotenv.load_dotenv()
injector = Injector()
conf = Config()

app = Http(__name__, conf=conf, router=injector.get(Router))
## injector再router 包内做了依赖注入，所有这里可以通过injector.get 获取

if __name__ == "__main__":
    app.run(debug=True)
