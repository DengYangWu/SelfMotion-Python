# -*- coding: utf-8 -*-#
import yaml
import sys
import os
from appium import webdriver
import time
import yaml
import threading
import config.join_meeting,config.log_out,config.log_in,config.exit_meeting

import HTMLTestRunner
#多进程工具包  与threading类似
import multiprocessing
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
#元素等待
from selenium.webdriver.support.ui import WebDriverWait
import os

import logging
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
#定位toast提示
def laction_toast_Demo(driver):
    print(driver)

    driver.find_element_by_id("cn.butel.redmeeting:id/login_pwd_ed").send_keys(1)
    driver.find_element_by_id("cn.butel.redmeeting:id/login_title").click()
    #time.sleep(2)
    driver.find_element_by_id("cn.butel.redmeeting:id/login_btn").click()
    toastmessage = "账号或密码错误"
    toast_loc = './/*[android.widget.FrameLayout(@text,"账号或密码错误")]'
    toast = WebDriverWait(driver, 5, 0.1).until(EC.presence_of_element_located((MobileBy.XPATH,toast_loc)))
    print(driver.find_element_by_xpath(toast).text)
    # driver.find_element_by_id("cn.butel.redmeeting:id/name_rl").click()
    # driver.find_element_by_id("cn.butel.redmeeting:id/save_btn").click()
    #toast_message = "参会名称修改成功";
    #message ='//*[@class=\'{}\']'.format(toast_message)
    #toast_element = driver.find_element_by_xpath("//*[@id='cn.butel.redmeeting.util.CustomToast']")
    #toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath("//*[@class='android.widget.Toast']"))
    #toast_element = WebDriverWait(driver, 1).until(lambda x: x.find_element_by_xpath(message))
    #text = driver.find_element_by_id("cn.butel.redmeeting:id/CustomToast").text
    #time.sleep(1)
    toast_element = driver.find_element_by_xpath("//*[@class='cn.butel.redmeeting.util.CustomToast']").text
    #toast_element = driver.find_element_by_xpath('//*[contains(@text, "参会名称修改成功")]')
    print(toast_element)