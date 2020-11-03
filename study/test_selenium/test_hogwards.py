# -*- coding: utf-8 -*-
# @Time     : 2020/11/2 23:42
# @Author   : tangjy
# @File     : test_hogwards.py

from selenium import webdriver


class TestHogwards:
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(executable_path="")       # driver未添加环境变量需要添加执行路径
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)      # 隐式等待，能简化代码


    def teardown(self):
        self.driver.quit()  # 回收

    def test_hogwards(self):
        self.driver.get("https://ceshiren.com/")    # 打开网址
        # 定位元素，对元素点击、


if __name__ == "__main__":
    pass
