# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 20:57
# @Author   : tangjy
# @File     : addmember_page.py
from selenium.webdriver.common.by import By

from study.pageobject.page.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member(self, name, account, phone_num):
        # input name
        self.find(By.ID, "username").send_keys(name)
        # input account
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        # input phone num
        self.find(By.ID, "memberAdd_phone").send_keys(phone_num)
        # click save
        self.find(By.LINK_TEXT, "保存").click()
        return True

    def get_member(self, name):
        titles_total = []
        while True:
            elements = self.finds(By.CLASS_NAME, "member_colRight_memberTable_td")
            # titles = []
            # for element in elements:
            #     titles.append(element.get_attribute("title"))
            titles = [element.get_attribute("title") for element in elements]
            # 找到，跳出循环
            if name in titles:
                return True

            # titles_total.extend(titles)
            pages:str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = pages.split("/", 1)
            # 当前最后一页，没找到
            if int(num) == int(total):
                return False
            else:
                # 当前不是最后一页，翻到下一页
                elem = self._driver.execute_script("return document.getElementsByClassName('ww_pageNav_info_arrowWrap js_next_page')[0]")
                elem.click()

        # return titles_total