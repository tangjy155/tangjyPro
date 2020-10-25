# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 22:08
# @Author   : tangjy
# @File     : tonglao.py


class TongLao:
    def __init__(self, hp, power):
        self._hp = hp
        self._power = power

    def see_people(self, name):
        if name == "WYZ":
            print("师弟！！！！")
        elif name == "LQS":
            print("师弟是我的！")
        elif name == "DCQ":
            print("叛徒！我杀了你")

    def fight_zms(self, enemy_hp, enemy_power):
        # 血量缩减一半、武力值提升10倍
        self._hp /= 2
        self._power *= 10

        # 一回合对打
        self._hp -= enemy_power
        enemy_hp -= self._power

        if self._hp > enemy_hp:
            print("我赢了")
        else:
            print("我输了")


if __name__ == "__main__":
    tonglao = TongLao(1000, 200)
    tonglao.fight_zms(2000, 500)