# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 1:23
# @Author   : tangjy
# @File     : contact_info_page.py
from appium.webdriver.common.mobileby import MobileBy

from practice.appium_wx.page.base_page import BasePge
from practice.appium_wx.page.contact_details_page import ContactDetailsPage


class ContactInfoPage(BasePge):
    def father_page(self):
        self._driver.find_element(MobileBy.ID, "com.tencent.wework:id/hv3").click()

    def goto_details(self):
        # click
        self._driver.find_element(MobileBy.ID, "com.tencent.wework:id/hvd").click()
        # 返回联系人详情页面
        return ContactDetailsPage(self._driver)