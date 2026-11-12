"""
@Time   : 2026/8/3  23:46
@AUTHOR : urchiola@163.com
@file   : app_handler.py
"""
import os
from flask import request, jsonify
from openai import OpenAI

from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json

class AppHandler:
    """应用控制器"""

    def completion(self):
        """聊天接口"""
        # 1. 提取从接口中获取的输入，POST
        req = CompletionReq()
        if not req.validate(): ### 如果不合格
            return validate_error_json(req.errors)
        query = request.json.get('query')
        # 2.
        client = OpenAI(
            # 使用 python-dotenv 会自动读取 .env 中api, 其他参数不会自动读取，例如，base_url

            base_url=os.getenv('GLOUTH_BASE_URL'),
            api_key=os.getenv('GLOUTH_LINK_KEY'),
        )

        # 新版写法
        response = client.responses.create(
            model="gpt-5.5",
            input=[
                {
                    "role": "system", "content": "你是OpenAI开发的聊天机器人，请根据用户的输入回复对应的信息",
                },
                {
                    "role": "user", "content": query
                }
            ],
            store=True,
        )

        # 旧版API 已不支持
        # completion = client.chat.completions.create(
        #     model="gpt-5.4-mini",
        #     input=[
        #         {
        #             "role": "system", "content": "你是OpenAI开发的聊天机器人，请根据用户的输入回复对应的信息",
        #         },
        #         {
        #             "role": "user", "content": query
        #         }
        #     ],
        # )
        # ountText = completion.choices[0].message.content

        outText = response.output_text

        return  success_json({ "content": outText })
    def ping(self):
        return {'ping': 'pong'}
