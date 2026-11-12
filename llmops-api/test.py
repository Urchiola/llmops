"""
@Time   : 2026/8/3  23:36
@AUTHOR : urchiola@163.com
@file   : test.py
"""
from injector import Injector, inject


class A:
    name: str = 'llmops'


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"class A的name:{self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
