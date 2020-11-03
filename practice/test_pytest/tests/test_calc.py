# -*- coding: utf-8 -*-
# @Time     : 2020/10/30 20:17
# @Author   : tangjy
# @File     : test_calc.py
import math

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
    def test_mul_none(self, a, b):
        with pytest.raises(Exception) as e_info:
            assert self.calc.mul(a, b)

    @allure.story("非法字符")
    @pytest.mark.parametrize('a, b', [
        ['Q', '/'],
        ['q', 2],
        [2, '/']
    ])
    def test_mul_abnormal(self, a, b):
        with pytest.raises(Exception) as e_info:
            assert self.calc.mul(a, b)

    @allure.story("整数")
    @pytest.mark.parametrize('a, b, c', [
        [6, 2, 12],
        [-3, -2, 6],
        [4, -2, -8]
    ])
    def test_mul_int(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("浮点数")
    @pytest.mark.parametrize('a, b, c', [
        [0.0001, 9.9, 0.00099],
        [1 / 3, 0.3, 0.3/3]
    ])
    def test_mul_float(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("分数和整数")
    @pytest.mark.parametrize('a, b, c', [
        [1 / 3, 3, 1]
    ])
    def test_mul_mix(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("表达式参数")
    @pytest.mark.parametrize('a, b, c', [
        [1 + 2, 3, 9],
        [2, 1 + 2, 6],
        [1 + 2, 1 + 3, 12]
    ])
    def test_mul_exp(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("零值")
    @pytest.mark.parametrize('a, b, c', [
        [0, 3, 0],
        [2, 0, 0],
        [0, 0, 0]
    ])
    def test_mul_zero(self, a, b, c):
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
    def test_mul_inf(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("零值和无限大")
    @pytest.mark.parametrize('a, b', [
        [float("inf"), 0 ],
        [0, float("inf")],
        [0, float("-inf")],
        [float("-inf"), 0]
    ])
    def test_mul_zero_and_inf(self, a, b, c):
        assert math.isnan(self.calc.mul(a, b))


@allure.feature("除法测试")
class TestDiv:
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
    def test_div_none(self, a, b):
        with pytest.raises(Exception) as e_info:
            assert self.calc.div(a, b)

    @allure.story("非法字符")
    @pytest.mark.parametrize('a, b', [
        ['Q', '/'],
        ['q', 2],
        [2, '/']
    ])
    def test_div_abnormal(self, a, b):
        with pytest.raises(Exception) as e_info:
            assert self.calc.div(a, b)

    @allure.story("整数")
    @pytest.mark.parametrize('a, b, c', [
        [6, 2, 3],
        [-3, -2, 1.5],
        [4, -2, -2]
    ])
    def test_div_int(self, a, b, c):
        assert self.calc.div(a, b) == c

    @allure.story("浮点数")
    @pytest.mark.parametrize('a, b, c', [
        [9.9, 0.1, 99.0],
        [0.6, 0.3, 2.0]
    ])
    def test_div_float(self, a, b, c):
        assert self.calc.div(a, b) == c

    @allure.story("分数和整数")
    @pytest.mark.parametrize('a, b, c', [
        [1 / 3, 3, 1/9]
    ])
    def test_div_mix(self, a, b, c):
        assert self.calc.div(a, b) == c

    @allure.story("表达式参数")
    @pytest.mark.parametrize('a, b, c', [
        [1 + 2, 3, 1],
        [6, 1 + 2, 2],
        [4 + 2, 1 + 3, 2]
    ])
    def test_div_exp(self, a, b, c):
        assert self.calc.div(a, b) == c

    @allure.story("零值")
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0, 0]
    ])
    def test_div_zero(self, a, b, c):
        with pytest.raises(Exception) as e_info:
            assert self.calc.div(a, b)

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
    def test_div_inf(self, a, b, c):
        assert self.calc.div(a, b) == c

    @allure.story("零值和无限大")
    @pytest.mark.parametrize('a, b', [
        [float("inf"), 0 ],
        [0, float("inf")],
        [0, float("-inf")],
        [float("-inf"), 0]
    ])
    def test_div_zero_and_inf(self, a, b, c):
        assert math.isnan(self.calc.div(a, b)) == True


class TestPros:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

    # 流程示例
    @allure.story("流程测试")
    def test_process(self):
        r1 = self.calc.mul(1, 2)
        r2 = self.calc.div(2, 1)
        assert r1 == 2
        assert r2 == 2


if __name__ == "__main__":
    pass
