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

def login_circulation(driver):

    #print("循环登录")
    int_i = 0
    i = 1
    while(True):
        #i = 1
        time.sleep(6)
        #print("123")
        driver.find_element_by_id("cn.butel.redmeeting:id/head_iv").click()
        driver.find_element_by_id("cn.butel.redmeeting:id/btn_logout").click()
        driver.find_element_by_id("cn.butel.redmeeting:id/dy_tv").click()
        driver.find_element_by_id("cn.butel.redmeeting:id/btn_right").click()
        driver.find_element_by_id("cn.butel.redmeeting:id/login_btn").click()
        int_i = int_i + i
        print("本轮执行次数为："+str(int_i))