# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 19:44
# @Author   : tangjy
# @File     : shape_oop.py
import math

# 形状类
class Shape:
    # 获取边长
    def get_sides(self):
        pass

    # 获取周长
    def get_circumference(self):
        pass

    # 获取面积
    def get_square(self):
        pass


# 三角形类
class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    # 获取三角形边长
    def get_sides(self):
        return [self._side_a, self._side_b, self._side_c]

    # 获取三角形的周长
    def get_circumference(self):
        circumference = self._side_a + self._side_b + self._side_c
        return circumference

    # 获取三角形的面积
    def get_square(self):
        value_a = self._side_a + self._side_b - self._side_c
        value_b = self._side_a + self._side_c - self._side_b
        value_c = self._side_b + self._side_c - self._side_a

        square = math.sqrt(self.get_circumference() * value_a * value_b * value_c) / 4
        return square


# 长方形类
class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self._side_a = side_a
        self._side_b = side_b

    # 获取长方形边长
    def get_sides(self):
        return [self._side_a, self._side_b]

    # 获取长方形的周长
    def get_circumference(self):
        circumference = self._side_a * 2 + self._side_b * 2
        return circumference

    # 获取长方形的面积
    def get_square(self):
        square = self._side_a * self._side_b
        return square


# 正方形类
class Square(Shape):
    def __init__(self, side):
        self._side = side

    # 获取正方形边长
    def get_sides(self):
        return [self._side]

    # 获取正方形的周长
    def get_circumference(self):
        circumference = self._side * 4
        return circumference

    # 获取正方形的面积
    def get_square(self):
        square = self._side * self._side
        return square


if __name__ == "__main__":
    triangle = Triangle(3, 4, 5)
    print(f"边长为{triangle.get_sides()}的三角形，"
          f"周长为：{triangle.get_circumference()}，"
          f"面积为：{triangle.get_square()}")

    rectangle = Rectangle(4, 5)
    print(f"边长为：{rectangle.get_sides()}的长方形，"
          f"周长为：{rectangle.get_circumference()}，"
          f"面积为：{rectangle.get_square()}")

    square = Square(4)
    print(f"边长为：{square.get_sides()}的正方形，"
          f"周长为：{square.get_circumference()}，"
          f"面积为：{square.get_square()}")