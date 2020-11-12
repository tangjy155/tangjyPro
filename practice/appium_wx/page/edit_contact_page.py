# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 1:35
# @Author   : tangjy
# @File     : edit_contact_page.py
from appium.webdriver.common.mobileby import MobileBy

from practice.appium_wx.page.base_page import BasePge


class EditContactPage(BasePge):
    def delete(self):
        # click
        self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                  'new UiScrollable(new UiSelector()'
                                  '.scrollable(true).instance(0))'
                                  '.scrollIntoView(new UiSelector()'
                                  '.text("删除成员").instance(0));').click()
        self._driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()