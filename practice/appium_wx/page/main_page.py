# -*- coding: utf-8 -*-
# @Time     : 2020/11/10 22:08
# @Author   : tangjy
# @File     : main_page.py
from appium.webdriver.common.mobileby import MobileBy

from practice.appium_wx.page.base_page import BasePge
from practice.appium_wx.page.contacts_page import ContactsPage


class MainPage(BasePge):
    _desired_cap = {}
    _desired_cap["platformName"] = "Android"
    _desired_cap["deviceName"] = "Android Emulator"
    _desired_cap["appPackage"] = "com.tencent.wework"
    _desired_cap["appActivity"] = ".launch.LaunchSplashActivity"
    _desired_cap["noReset"] = "true"

    def click_contact(self):
        # click
        #self.find(MobileBy.XPATH, "//*[@text='通讯录']/../..").click()
        self._driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 进入通讯录界面
        return ContactsPage(self._driver)