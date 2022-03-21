import time
#import Include.Runner
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from Include import Runner

def open(driver):
    print("试图打开语音")
    driver.find_element_by_id("demo.com.butel.redmeeting:id/mic_setting_switch").click()
    print("点击完毕")
def close(driver):
    print("试图关闭语音")
    driver.find_element_by_id("demo.com.butel.redmeeting:id/mic_setting_switch").click()
    print("点击完毕")