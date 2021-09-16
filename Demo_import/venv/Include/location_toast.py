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

#定位toast提示
def laction_toast_Demo(driver):
    #print(driver)
    driver.find_element_by_id("cn.butel.redmeeting:id/head_iv").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/gotomyfilecard_rl").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/name_rl").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/save_btn").click()
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