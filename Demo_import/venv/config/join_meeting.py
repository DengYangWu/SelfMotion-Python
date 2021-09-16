from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import threading
import time

def Join_meeting(driver):
    # 自动登录 进入会议脚本
    driver.find_element_by_id("cn.butel.redmeeting:id/join_meeting_ly").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/meetingid_input_edit").send_keys("30234379")
    driver.find_element_by_id("cn.butel.redmeeting:id/join_meeting_btn").click()