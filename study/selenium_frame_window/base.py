# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 9:40
# @Author   : tangjy
# @File     : base.py
from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()