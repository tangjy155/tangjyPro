# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 19:36
# @Author   : tangjy
# @File     : test_appium_case.py
from appium import webdriver

desired_caps = {
  "platformName": "android",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el3.click()
driver.back();

