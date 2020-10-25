# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 21:13
# @Author   : tangjy
# @File     : furniture_oop.py


# 家具类
class Furniture:
    pass


# 桌子类
class Table(Furniture):
    def __init__(self):
        print("我是一张桌子！")


# 椅子类
class Chair(Furniture):
    def __init__(self):
        print("我是一张椅子！")


if __name__ == "__main__":
    table = Table()
    chair = Chair()
