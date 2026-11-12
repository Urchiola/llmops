"""
@Time   : 2026/8/10  15:33
@AUTHOR : urchiola@163.com
@file   : example.py
"""
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.6",
    input="Write a one-sentence bedtime story about a unicorn.",
)

print(response.output_text)