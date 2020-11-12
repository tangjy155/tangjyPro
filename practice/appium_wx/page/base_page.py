# -*- coding: utf-8 -*-
# @Time     : 2020/11/10 22:08
# @Author   : tangjy
# @File     : base_page.py
from appium import webdriver


class BasePge:
    _desired_cap = {}

    def __init__(self, driver=None):
        if driver is not None:
            self._driver = driver
        if self._desired_cap != {}:
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", self._desired_cap)

        self._driver.implicitly_wait(30)

    def __del__(self):
        # self._driver.quit()
        pass

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def find(self, by, locator):
        return self._driver.find_elements(by, locator)

