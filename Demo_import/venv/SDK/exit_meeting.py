from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import threading
import time
#import Include.Runner
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions

def exit_meeting(driver):
    print("企图退出会议~~~~~~~")
    time.sleep(2)
    driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
    time.sleep(1)
    #TouchAction(driver).tap(x=800,y=488).release().perform()
    driver.find_element_by_id("demo.com.butel.redmeeting:id/header_tool_view_back_tv").click()
    driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_sure").click()
