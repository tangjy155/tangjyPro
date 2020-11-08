# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 19:50
# @Author   : tangjy
# @File     : base_page.py
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_option = webdriver.ChromeOptions()
            chrome_option.debugger_address = "127.0.0.1:9222"

            self._driver = webdriver.Chrome(options=chrome_option)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    def __del__(self):
        self._driver.quit()

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)