# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 19:05
# @Author   : tangjy
# @File     : test_file.py
from time import sleep

from study.selenium_frame_window.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_id("sttb").click()
        self.driver.find_element_by_id("stfile").send_keys("C:\\Users\\33155\\Pictures\\PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png")
        sleep(3)