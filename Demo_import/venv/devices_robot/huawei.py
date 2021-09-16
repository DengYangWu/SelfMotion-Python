from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import threading

def dev(devices):
    caps = {}
    caps["platformName"] = "Android"
    caps["deviceName"] = devices
    caps["appPackage"] = "cn.butel.redmeeting"
    caps["appActivity"] = "cn.butel.redmeeting.boot.SplashActivity"
    caps["noReset"] = "true"
    caps["automationName"] = "UiAutomator1"
    caps["skipServerInstallation"] = "true"
    caps["skipDeviceInitialization"] = "true"
    caps["newCommandTimeout"] = "600"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


    return devices
    #return driver

def exist():
    print(1)
# if __name__ == '__main__':
#     dev()