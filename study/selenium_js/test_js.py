# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 16:09
# @Author   : tangjy
# @File     : test_js.py
from time import sleep

from study.selenium_frame_window.base import Base


class TestJS(Base):
    def js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("测试")
        # self.driver.find_element_by_id("su").click()
        elem = self.driver.execute_script("return document.getElementById('su')")
        elem.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        self.driver.find_element_by_link_text("下一页 >").click()
        sleep(3)

        # for code in [
        #     'return document.title', 'return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a = document.getElementById('train_date');"
                                   "a.removeAttribute('readonly');"
                                   "a.value = '2020-12-03'")
        sleep(3)