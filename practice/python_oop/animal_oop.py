# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 18:41
# @Author   : tangjy
# @File     : animal_oop.py


# 动物类
class Animal:
    def __init__(self, color):
        self._color = color

    # 获取动物颜色
    def get_color(self):
        # print(self._color)
        return self._color

    def speak(self):
        print("动物叫~~~~~~")


# 猫类
class Cat(Animal):
    def speak(self):
        color = self.get_color()
        print(f"我是{color}的猫咪，我喵喵叫~~")


# 狗类
class Dog(Animal):
    def speak(self):
        print(f"我是{self._color}的小狗，我汪汪叫~~")


if __name__ == "__main__":
    kitty = Cat("白色")
    kitty.speak()

    puppy = Dog("黑色")
    puppy.speak()

    animal = Animal("不知道颜色")
    animal.speak()
