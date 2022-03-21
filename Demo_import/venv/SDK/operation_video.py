import time
#import Include.Runner
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from Include import Runner
def open_video(driver):
    print("试图打开摄像头~~~~")
    driver.find_element_by_id("demo.com.butel.redmeeting:id/carema_setting_switch").click()
    print("点击完毕")

def close_video(driver):
    print("试图关闭摄像头~~~~")
    driver.find_element_by_id("demo.com.butel.redmeeting:id/carema_setting_switch").click()
    print("点击完毕")