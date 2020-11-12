# -*- coding: utf-8 -*-
# @Time     : 2020/11/10 22:09
# @Author   : tangjy
# @File     : contacts_page.py
from appium.webdriver.common.mobileby import MobileBy

from practice.appium_wx.page.add_contact_page import AddContactPage
from practice.appium_wx.page.base_page import BasePge
from practice.appium_wx.page.contact_info_page import ContactInfoPage
from practice.appium_wx.page.search_contact_page import SearchContactPage


class ContactsPage(BasePge):
    def click_add_contact(self):
        # click
        # self.find(MobileBy.ANDROID_UIAUTOMATOR,
        self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # 返回手动添加成员页面
        return AddContactPage(self._driver)

    def click_contact(self, name):
        # click
        self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                   'new UiScrollable(new UiSelector()'
                                   '.scrollable(true).instance(0))'
                                   '.scrollIntoView(new UiSelector()'
                                   '.textContains("test").instance(0));').click()
        # 返回联系人界面
        return ContactInfoPage(self._driver)

    def click_search_contact(self):
        # click
        self._driver.find_element(MobileBy.ID, "com.tencent.wework:id/hvn").click()
        # 返回搜索联系人页面
        return SearchContactPage(self._driver)