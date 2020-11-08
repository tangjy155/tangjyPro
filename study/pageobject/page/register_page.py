# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 20:03
# @Author   : tangjy
# @File     : register_page.py
from study.pageobject.page.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/register_wx?from=myhome"

    def register(self):

        # input company name
        self.find(By.ID, "corp_name").send_keys("aaa")
        # input phone
        self.find(By.ID, "register_tel").send_keys("1111")
        # register
        self.find(By.ID, "submit_btn").click()
