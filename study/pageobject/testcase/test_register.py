# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 20:36
# @Author   : tangjy
# @File     : test_register.py
from study.pageobject.page.main_page import MainPage


class TestRegister:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    def test_register(self):
        # result = self.main.goto_login().goto_register()
        result = self.main.goto_register().register()
        # assert result