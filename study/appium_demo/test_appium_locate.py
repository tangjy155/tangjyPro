# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 20:05
# @Author   : tangjy
# @File     : test_appium_locate.py
import time

from appium import webdriver

desired_caps = {
    "platformName": "android",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".common.MainActivity",
    "noReset": 'true',
    "dontStopAppOnReset": 'true',
    "skipDeviceInitialization": 'true'
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.back()
driver.back()
time.sleep(3)

driver.quit()