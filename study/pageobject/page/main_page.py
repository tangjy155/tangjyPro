# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 19:57
# @Author   : tangjy
# @File     : main_page.py
from selenium.webdriver.common.by import By

from study.pageobject.page.base_page import BasePage
from study.pageobject.page.login_page import LoginPage
from study.pageobject.page.register_page import RegisterPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        # click register
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # 进入注册页面
        return RegisterPage(self._driver)

    def goto_login(self):
        # click login
        self.find((By.CSS_SELECTOR, ".index_top_operation_loginBtn")).click()
        # 进入登陆页面
        return LoginPage(self._driver)