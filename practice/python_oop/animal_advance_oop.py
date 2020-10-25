# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 21:29
# @Author   : tangjy
# @File     : animal_advance_oop.py.py


class Animal:
    def __init__(self, name = None, speed = None):
        self._name = name
        self._speed = speed

    def get_speed_behavior(self):
        pass


class Cat(Animal):
    def __init__(self, name, speed, color):
        super().__init__(name, speed)
        self._color = color

    def get_speed_behavior(self):
        print(f"{self._name}在地上跑的速度为{self._speed}")
        return self._speed


class Bird(Animal):
    def __init__(self, name, speed, color):
        super().__init__(name, speed)
        self._color = color

    def get_speed_behavior(self):
        print(f"{self._name}在天上飞的速度为{self._speed}")
        return self._speed


if __name__ == "__main__":
    kitty = Cat("kitty", 10, "白色")
    kitty.get_speed_behavior()

    bird = Bird("小鸟", 20, "灰色")
    bird.get_speed_behavior()
