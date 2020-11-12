# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 1:31
# @Author   : tangjy
# @File     : contact_details_page.py
from appium.webdriver.common.mobileby import MobileBy

from practice.appium_wx.page.base_page import BasePge
from practice.appium_wx.page.edit_contact_page import EditContactPage


class ContactDetailsPage(BasePge):
    def click_edit(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        # 返回编辑成员页面
        return EditContactPage(self._driver)