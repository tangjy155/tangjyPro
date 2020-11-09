# -*- coding: utf-8 -*-
# @Time     : 2020/11/9 21:09
# @Author   : tangjy
# @File     : test_locate_pytest.py
from appium import webdriver


class TestSearch:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            "noReset": 'true',
            "dontStopAppOnReset": 'true',
            "skipDeviceInitialization": 'true',
            "unicodeKeyboard": 'true',
            "resetKeyboard": 'true'
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        """
        1. 打开雪球app
        2. 点击搜索输入框
        3. 搜索输入框里输入 “阿里巴巴”
        4. 搜索结果中选择 ”阿里巴巴“，然后进行点击
        5. 获取这只上相关 阿里巴巴的股价，并判断 这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200