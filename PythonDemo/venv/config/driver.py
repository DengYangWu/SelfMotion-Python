from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import threading
import time

def Join_meeting(driver):
    # 自动登录 进入会议脚本
    driver.find_element_by_id("cn.butel.redmeeting:id/join_meeting_ly").click()
    driver.find_element_by_id("cn.butel.redmeeting:id/meetingid_input_edit").send_keys("10231070")
    driver.find_element_by_id("cn.butel.redmeeting:id/join_meeting_btn").click()
# caps = {
#     'platformName':'Android',
#     'deviceName':'192.168.1.108:5556',
#     'platformVersion':'10',
#     'appPackage':'cn.butel.redmeeting',
#     'appActivity':'cn.butel.redmeeting.boot.SplashActivity',
# }
# caps2 = {
#     'platformName':'Android',
#     'deviceName':'192.168.1.104:5557',
#     'platformVersion':'10',
#     'appPackage':'cn.butel.redmeeting',
#     'appActivity':'cn.butel.redmeeting.boot.SplashActivity',
# }
# # caps["platformName"] = "Android"
# # caps["platformVersion"] = "10"
# # caps["deviceName"] = "华为mate30"
# # caps["appPackage"] = "cn.butel.redmeeting"
# # caps["appActivity"] = "cn.butel.redmeeting.boot.SplashActivity"
# # caps["noReset"] = "true"
# # #caps["automationName"] = "UiAutomator1"
# # caps["skipServerInstallation"] = "true"
# # caps["skipDeviceInitialization"] = "true"
# # driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# def task1():
#     driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#     time.sleep(20)
#     print(driver.contexts)
#     driver.quit()
# 
# def task2():
#     driver = webdriver.Remote("http://localhost:4725/wd/hub", caps2)
#     time.sleep(20)
#     print(driver.contexts)
#     driver.quit()
# 
# threads = []
# t1 = threading.Thread(target=task1)
# threads.append(t1)
# 
# t2 = threading.Thread(target=task2)
# threads.append(t2)
# 
# if __name__ == '__main__':
#     for t in threads:
#         t.start()