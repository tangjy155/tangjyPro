# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 0:49
# @Author   : tangjy
# @File     : search_contact_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from practice.appium_wx.page.base_page import BasePge
from practice.appium_wx.page.contact_details_page import ContactDetailsPage


class SearchContactPage(BasePge):
    def father_page(self):
        self._driver.find_element(MobileBy.ID, "com.tencent.wework:id/hv3").click()

    def get_contacts_num(self, name):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)

        WebDriverWait(self._driver, 10, 0.5).until(
            expected_conditions.visibility_of_element_located((MobileBy.ID, "com.tencent.wework:id/d9v")))
        print(f'name:{name}')

        list = self._driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.textContains(\"" + name + "\").instance(0));')
        print(f"list:{list}")
        return len(list)

    def goto_contact(self, name):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)

        WebDriverWait(self._driver, 10, 0.5).until(
            expected_conditions.visibility_of_element_located((MobileBy.ID, "com.tencent.wework:id/d9v")))

        self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                   'new UiScrollable(new UiSelector()'
                                   '.scrollable(true).instance(0))'
                                   '.scrollIntoView(new UiSelector()'
                                   '.textContains(\"" + name + "\").instance(0));').click()

        return ContactDetailsPage(self._driver)

