# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 21:02
# @Author   : tangjy
# @File     : test_contact.py
from study.pageobject.page.index_page import IndexPage


class TestContact():
    def setup(self):
        self.index = IndexPage()

    def teardown(self):
        pass

    def test_add_contact(self):
        name = "zzz"
        account = "zzz"
        phone_num = "13800000099"

        add_member_page = self.index.click_add_member()
        add_member_page.add_member(name, account, phone_num)
        result = add_member_page.get_member(name)
        assert result == True
