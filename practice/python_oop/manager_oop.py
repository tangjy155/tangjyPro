# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 21:29
# @Author   : tangjy
# @File     : manager_oop.py
import time

from practice.python_oop.animal_advance_oop import Cat, Bird


class Manager:
    def __init__(self, animal):
        self.animal = animal

    def record_time(self):
        self._time = time.asctime(time.localtime(time.time()))
        print(f"喂{self.animal._name}的时间为{self._time}")
        self.animal.get_speed_behavior()


if __name__ == "__main__":
    kitty = Cat("kitty", 10, "白色")
    bird = Bird("小鸟", 20, "黑色")

    Manager(kitty).record_time()
    Manager(bird).record_time()
