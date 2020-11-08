# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 20:05
# @Author   : tangjy
# @File     : login_page.py
from selenium.webdriver.common.by import By

from study.pageobject.page.base_page import BasePage
from study.pageobject.page.register_page import RegisterPage


class LoginPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"

    def scan(self):
        pass

    def goto_register(self):
        # click register
        self.find(By.CSS_SELECTOR, "login_registerBar_link").click()
        return RegisterPage(self._driver)
