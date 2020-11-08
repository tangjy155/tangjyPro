# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 20:52
# @Author   : tangjy
# @File     : index_page.py
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from study.pageobject.page.addmember_page import AddMemberPage
from study.pageobject.page.base_page import BasePage


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def click_add_member(self):
        # click add member
        self.find(By.LINK_TEXT, "添加成员").click()
        return AddMemberPage(self._driver)