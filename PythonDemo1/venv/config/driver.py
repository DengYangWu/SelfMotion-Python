from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import threading
import time


# tryCatch
from selenium.common.exceptions import NoSuchElementException
# 点击
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

def Join_meeting(driver):
    # 自动登录 进入会议脚本
    driver.find_element_by_id("cn.butel.redmeeting:id/join_meeting_ly").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/meetingid_input_edit").send_keys("10230995")
    driver.find_element_by_id("cn.butel.redmeeting:id/join_meeting_btn").click()
# caps = {
#     'platformName': 'Android',
#     'deviceName': '华为mate30',
#     'platformVersion': '10',
#     'appPackage': 'cn.butel.redmeeting',
#     'appActivity': 'cn.butel.redmeeting.boot.SplashActivity',
#     'noReset': 'true',
#     'udid': '192.168.1.107:5556',
#     'skipServerInstallation': 'true',
#     'skipDeviceInitialization': 'true',
#     'automationName': 'UiAutomator1',
# }
# caps2 = {
#     'platformName': 'Android',
#     'deviceName': '华为9a',
#     'platformVersion': '10',
#     'appPackage': 'cn.butel.redmeeting',
#     'appActivity': 'cn.butel.redmeeting.boot.SplashActivity',
#     'noReset': 'true',
#     'udid': '192.168.1.113:5557',
#     'skipServerInstallation': 'true',
#     'skipDeviceInitialization': 'true',
#     'automationName': 'UiAutomator1',
# }
#
#
# # caps["platformName"] = "Android"
# # caps["platformVersion"] = "10"
# # caps["deviceName"] = "华为mate30"
# # caps["appPackage"] = "cn.butel.redmeeting"
# # caps["appActivity"] = "cn.butel.redmeeting.boot.SplashActivity"
# # caps["noReset"] = "true"
# # #caps["automationName"] = "UiAutomator1"
# # caps["skipServerInstallation"] = "true"
# # caps["skipDeviceInitialization"] = "true"
# # driver = webdriver.Remote("http://localhost:55570/wd/hub", caps)
# # driver = webdriver.Remote("http://localhost:55580/wd/hub", caps2)
# def task1():
#     driver = webdriver.Remote("http://localhost:55570/wd/hub", caps)
#     time.sleep(20)
#     driver.quit()
#
# def task2():
#     driver = webdriver.Remote("http://localhost:55580/wd/hub", caps2)
#     print(caps2)
#     time.sleep(20)
#     driver.quit()
#
# threads = []
#
# t1 = threading.Thread(target=task1())
#     # threads.append(t1)
# t2 = threading.Thread(target=task2())
#     # threads.append(t2)
# t1.start()
# t2.start()
#
#
#
# # def setUp(self):
# #     self.device = webdriver.Remote(webdriver_remote,sys_pras);
#
#
# # def __init__(self, device):
# #     self.device = device
# # aa = getport()
# # self.ap = aa[0]
# # self.bp = aa[1]
#
#
# print("退出主线程")
