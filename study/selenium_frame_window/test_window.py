# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 10:23
# @Author   : tangjy
# @File     : test_window.py
import time

from study.selenium_frame_window.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登陆").click()
        self.driver.find_element_by_link_text("立即注册").click()
        time.sleep(3)