# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 0:22
# @Author   : tangjy
# @File     : add_contact_by_input.py
from appium.webdriver.common.mobileby import MobileBy

from practice.appium_wx.page.base_page import BasePge


class AddContactByInput(BasePge):
    def add_by_input(self, name, gender, phone_num):
        # input name
        self._driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(
            name)
        # select sex
        self._driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        if gender == "男":
            self._driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self._driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        # input phone num
        self._driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone_num)
        self._driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
