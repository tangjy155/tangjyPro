# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 10:34
# @Author   : tangjy
# @File     : test_wx.py
'''
复用浏览器，获取cookies，存入db
使用db中cookies登陆
完成添加联系人，加上断言验证
'''
import shelve
from time import sleep

from selenium import webdriver
import pytest
import allure


@allure.story("测通讯录添加成功")
class TestWX:
    def get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        cookies = self.driver.get_cookies()

        # shelve 模块， python 自带的对象持久化存储
        db = shelve.open('cookies')
        db['cookie'] = cookies

    def login(self):
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        # print(cookies)
        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 加入cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新当前页面
        self.driver.refresh()

    def setup(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.debugger_address = '127.0.0.1:9222'

        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        # self.get_cookies()
        self.login()

    def teardown(self):
        self.driver.quit()

    def add_member(self, name, account, phone):
        self.driver.find_element_by_link_text("添加成员").click()
        self.driver.find_element_by_id("username").send_keys(name)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(account)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(phone)
        self.driver.find_element_by_link_text("保存").click()

    @allure.feature("添加新成员")
    @pytest.mark.parametrize('name, account, phone', [
        ["test_a", "test_a", "13811111111"],
        ["test_b", "test_b", "13811111112"]
    ])
    def test_add_member_new(self, name, account, phone):
        self.add_member(name, account, phone)

        self.driver.find_element_by_link_text("通讯录").click()
        data = self.driver.find_elements_by_class_name("member_colRight_memberTable_td")
        result = False
        for d in data:
            if d.text and d.text == phone:
                result = True
                break
        assert result == True

    @allure.feature("添加新成员，用户名同名")
    @pytest.mark.parametrize('name, account, phone', [
        ["test_a", "test_c", "13811111113"]
    ])
    def test_add_member_name(self, name, account, phone):
        self.add_member(name, account, phone)

        self.driver.find_element_by_link_text("通讯录").click()
        data = self.driver.find_elements_by_class_name("member_colRight_memberTable_td")
        result = False
        for d in data:
            if d.text and d.text == phone:
                result = True
                break
        assert result == True

    @allure.feature("添加新成员，账号同名")
    @pytest.mark.parametrize('name, account, phone', [
        ["test_d", "test_a", "13811111114"]
    ])
    def test_add_member_account(self, name, account, phone):
        self.add_member(name, account, phone)

        data = self.driver.find_elements_by_class_name("ww_inputWithTips_tips")
        result = False
        for d in data:
            if d.text and d.text == '该帐号已被“test_a”占有':
                result = True
                break
        assert result == True

    @allure.feature("添加新成员，手机号同名")
    @pytest.mark.parametrize('name, account, phone', [
        ["test_e", "test_e", "13811111111"]
    ])
    def test_add_member_phone(self, name, account, phone):
        self.add_member(name, account, phone)

        data = self.driver.find_elements_by_class_name("ww_inputWithTips_tips")
        result = False
        for d in data:
            if d.text:
                print(d.text)
            if d.text and d.text == '该手机号已被“test_a”占有':
                result = True
                break
        assert result == True
