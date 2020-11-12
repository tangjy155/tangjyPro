# -*- coding: utf-8 -*-
# @Time     : 2020/11/10 21:35
# @Author   : tangjy
# @File     : test_add_contact.py
from practice.appium_wx.page.main_page import MainPage


class TestAddContact:
    def setup(self):
        self.main_page = MainPage()

    def teardown(self):
        pass

    def test_add_contact(self):
        name = "1216"
        gender = "女"
        phone_num = "13812340004"
        add_member = self.main_page.click_contact().click_add_contact()
        add_member.click_add_by_input().add_by_input(name, gender, phone_num)
        assert add_member.get_add_result() == True