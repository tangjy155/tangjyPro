# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 22:19
# @Author   : tangjy
# @File     : xuzhu.py
from practice.python_oop.tonglao import TongLao


class XuZhu(TongLao):
    def read(self):
        print("罪过罪过!")

    # 只有read方法，继承的fight_zms也被重写
    def fight_zms(self, enemy_hp, enemy_power):
        self.read()

    # 只有read方法，继承的see_people也被重写
    def see_people(self, name):
        self.read()

if __name__ == "__main__":
    xuzhu = XuZhu(1000, 200)
    # xuzhu.read()
    xuzhu.fight_zms(2000, 500)