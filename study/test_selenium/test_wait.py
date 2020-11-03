# -*- coding: utf-8 -*-
# @Time     : 2020/11/3 19:52
# @Author   : tangjy
# @File     : test_wait.py
from time import sleep

from selenium import webdriver


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_wait(self):
        sleep(3)
        print("hello")



if __name__ == "__main__":
    pass
