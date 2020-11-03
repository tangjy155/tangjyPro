# -*- coding: utf-8 -*-
# @Time     : 2020/11/3 20:56
# @Author   : tangjy
# @File     : test_webwx.py
import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWebwx():
    def setup(self):
        # 复用浏览器
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(Options=option)

    def teardown(self):
        self.driver.quit()

    def test_webwx(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID, "").click()

    def test_cookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)

        self.driver.get("weixin")

        for cookie in cookies:
            if 'expire' in cookie.keys:
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # self.driver.get("weixin")

    def test_case2(self):
        cookies = self.driver.get_cookies()
        # shelve 模块， python自带的对唱持久化存储
        # 保存到了本地文件
        db = shelve.open('cookies')
        db['cookie'] = cookies  # 2进制存储
        db.close()

        # 获取本地数据
        db = shelve.open('cookies')
        cookies = db['cookie']  # 2进制存储
        db.close()
        # 无痕打开新页面

        # 加入cookie

        # 刷新当前页面，获取登陆状态


if __name__ == "__main__":
    pass
