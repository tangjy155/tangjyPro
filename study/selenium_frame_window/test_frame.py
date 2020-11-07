# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 9:39
# @Author   : tangjy
# @File     : test_frame.py
import time

from study.selenium_frame_window.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

        # iframeResult
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)

        # time.sleep(3)
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_id("submitBTN").click()
        time.sleep(3)