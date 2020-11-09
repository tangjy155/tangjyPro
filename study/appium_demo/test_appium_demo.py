# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 14:12
# @Author   : tangjy
# @File     : test_appium_demo.py
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.mumu.launcher'
desired_caps['appActivity'] = 'com.mumu.launcher.Launcher'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.quit()