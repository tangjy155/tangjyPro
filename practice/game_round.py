# -*- coding: utf-8 -*-
# @Time     : 2020/10/24 0:33
# @Author   : tangjy
# @File     : game_round.py
import random


def fight(enemy_hp, enemy_power, my_hp, my_power):
    # 循环，游戏可进行多轮
    while True:
        my_hp -= enemy_power
        enemy_hp -= my_power

        # 判断输赢,有结果则跳出循环
        if my_hp <= 0:
            # 打印我和敌人的剩余hp
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量为{enemy_hp}")
            print("我输了!")
            break;
        elif enemy_hp <= 0:
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量为{enemy_hp}")
            print("我赢了!")
            break;

if __name__ == "__main__":
    # 列表推导式生成敌人初始的hp、power
    hp = [x for x in range(990, 1010)]
    random.shuffle(hp)
    enemy_hp = random.choice(hp)
    power = [y for y in range(190, 210)]
    enemy_power = random.choice(power)

    my_hp = random.randrange(990, 1010, 1)
    my_power = random.randrange(190, 210, 1)

    print(f"敌人的初始血量为{enemy_hp}")
    print(f"敌人的初始攻击力为{enemy_power}")

    print(f"我的初始血量为{my_hp}")
    print(f"我的初始攻击力为{my_power}")

    fight(enemy_hp, enemy_power, my_hp, my_power)