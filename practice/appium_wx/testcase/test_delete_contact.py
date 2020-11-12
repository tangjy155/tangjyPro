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
        num_menber1 = search_page.get_contacts_num(name)
        print(f"num_menber1:{num_menber1}")

        contact_info = search_page.goto_contact(name)
        contact_info.goto_details().click_edit().delete()
        contact_info.father_page()
        search_page.father_page()

        search_page = contacts.click_search_contact()
        num_menber2 = search_page.get_contacts_num(name)
        search_page.father_page()
        print(f"num_menber2:{num_menber2}")


        assert num_menber1 > num_menber2