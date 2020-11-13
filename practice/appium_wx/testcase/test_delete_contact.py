# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 1:38
# @Author   : tangjy
# @File     : test_delete_contact.py
from practice.appium_wx.page.main_page import MainPage


class TestDeleteContact:
    def setup(self):
        self.main_page = MainPage()

    def test_delete_contact(self):
        name = "111"
        contacts = self.main_page.click_contact()

        search_page = contacts.click_search_contact()
        num_member1 = search_page.get_contacts_num(name)

        assert num_member1 > 0

        print(f"num_member1:{num_member1}")

        contact_info = search_page.goto_contact(name)
        contact_info.goto_details().click_edit().delete()

        num_member2 = search_page.get_contacts_num(name)
        print(f"num_member2:{num_member2}")

        assert num_member1 > num_member2