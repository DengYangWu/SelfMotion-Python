import yaml
import os
from appium import webdriver
import unittest
import time
import yaml
import os
import threading

#退出登录脚本
def log(driver):
    driver.find_element_by_id("cn.butel.redmeeting:id/head_iv").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/btn_logout").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/dy_tv").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/btn_right").click()
