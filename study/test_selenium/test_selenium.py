# -*- coding: utf-8 -*-
# @Time     : 2020/11/2 22:47
# @Author   : tangjy
# @File     : test_selenium.py


import selenium
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")


if __name__ == "__main__":
    pass
