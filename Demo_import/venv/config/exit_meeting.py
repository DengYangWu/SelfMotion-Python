import yaml
import os
from appium import webdriver
import unittest
import time
import yaml
import os
import threading

#退出会议
def exit(driver):
    driver.find_element_by_id("cn.butel.redmeeting:id/meeting_mode_speak_mode_view").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/header_tool_view_back_tv").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/tv_sure").click()
    