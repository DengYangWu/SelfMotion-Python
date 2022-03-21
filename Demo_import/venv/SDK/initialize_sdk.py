import sys
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import threading
import time
#import Include.Runner
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions

def init(driver):
    print("SDK在初始化中.....")
    driver.find_element_by_id("demo.com.butel.redmeeting:id/init_rl").click()
    time.sleep(6)
    TouchAction(driver).press(x=45,y=1069).move_to(x=0,y=370).release().perform()
    time.sleep(3)
