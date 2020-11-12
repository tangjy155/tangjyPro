# -*- coding: utf-8 -*-
# @Time     : 2020/11/10 22:10
# @Author   : tangjy
# @File     : add_contact_page.py
from appium.webdriver.common.mobileby import MobileBy

from practice.appium_wx.page.add_contact_by_input import AddContactByInput
from practice.appium_wx.page.base_page import BasePge


class AddContactPage(BasePge):
    def click_add_by_input(self):
        # click
        # self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self._driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 返回手动输入添加联系人页面
        return AddContactByInput(self._driver)

    def get_add_result(self):
        result = self._driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        print(f"保存结果：{result}")
        if result == "添加成功":
            return True
        else:
            return False