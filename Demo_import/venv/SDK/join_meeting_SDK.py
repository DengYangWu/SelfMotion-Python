from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import threading
import time
#import Include.Runner
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
def Join_meeting(driver):
    # 自动登录 进入会议脚本
    driver.find_element_by_id("demo.com.butel.redmeeting:id/meetingId_et").clear()
    driver.find_element_by_id("demo.com.butel.redmeeting:id/meetingId_et").send_keys("30223658")
    #e1 = driver.find_element_by_id("demo.com.butel.redmeeting:id/init_rl")
    TouchAction(driver).press(x=45,y=1069).move_to(x=0,y=370).release().perform()
    time.sleep(3)
    driver.find_element_by_id("demo.com.butel.redmeeting:id/joinMeeting_rl").click()