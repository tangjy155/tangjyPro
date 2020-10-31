# -*- coding: utf-8 -*-
# @Time     : 2020/10/30 20:17
# @Author   : tangjy
# @File     : test_calc.py


import pytest
import allure

from practice.test_pytest.core.calc import Calc


@allure.feature("乘法测试")
class TestMul:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

    @allure.story("空值")
    @pytest.mark.parametrize('a, b', [
        [None, None],
        [None, 2],
        [2, None]
    ])
    def test_mul(self, a, b, c):
        with pytest.raises(Exception) as e_info:
            self.calc.mul(a, b)

    @allure.story("非法字符")
    @pytest.mark.parametrize('a, b', [
        ['Q', '/'],
        ['q', 2],
        [2, '/']
    ])
    def test_mul(self, a, b):
        with pytest.raises(Exception) as e_info:
            self.calc.mul(a, b)

    @allure.story("整数")
    @pytest.mark.parametrize('a, b', [
        [6, 2],
        [-3, -2],
        [4, -2]
    ])
    def test_mul(self, a, b):
        with pytest.raises(Exception) as e_info:
            self.calc.mul(a, b)

    @allure.story("浮点数")
    @pytest.mark.parametrize('a, b', [
        [0.0000000000000000000000001, 9.9],
        [1 / 3, 0.3]
    ])
    def test_mul(self, a, b):
        with pytest.raises(Exception) as e_info:
            self.calc.mul(a, b)

    @allure.story("分数和整数")
    @pytest.mark.parametrize('a, b, c', [
        [1 / 3, 3, 1]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("表达式参数")
    @pytest.mark.parametrize('a, b, c', [
        [1 + 2, 3, 9],
        [2, 1 + 2, 6],
        [1 + 2, 1 + 3, 12]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("零值")
    @pytest.mark.parametrize('a, b, c', [
        [0, 3, 0],
        [2, 0, 0],
        [0, 0, 0]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("无限大")
    @pytest.mark.parametrize('a, b, c', [
        [float("inf"), 3, float("inf")],
        [2, float("inf"), float("inf")],
        [float("inf"), -3, float("-inf")],
        [-2, float("inf"), float("-inf")],
        [2, float("-inf"), float("-inf")],
        [float("-inf"), 3, float("-inf")],
        [-2, float("-inf"), float("inf")],
        [float("-inf"), -3, float("inf")],
        [float("inf"), float("inf"), float("inf")],
        [float("-inf"), float("inf"), float("-inf")],
        [float("inf"), float("-inf"), float("-inf")],
        [float("-inf"), float("-inf"), float("inf")]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("零值和无限大")
    @pytest.mark.parametrize('a, b, c', [
        [float("inf"), 0, 0],
        [0, float("inf"), 0],
        [0, float("-inf"), 0],
        [float("-inf"), 0, 0]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c


class TestDiv:
    # 空值
    # 非法字符输入
    # 整数
    # 浮点数
    # 正、负无限大
    # 零值
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0.2, 0],
        [0, 0]
    ])
    @allure.story("除法测试")
    def test_div(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)


class TestPros:
    # 流程示例
    @allure.story("流程测试")
    def test_process(self):
        r1 = self.calc.mul(1, 2)
        r2 = self.calc.div(2, 1)
        assert r1 == 2
        assert r2 == 2


if __name__ == "__main__":
    pass
