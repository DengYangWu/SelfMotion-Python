# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import threading
from config import driver

# driver.caps
# driver.caps2
# task1 = driver.task1()
# print(task1)
# task2 = driver.task2()
# threads = driver.threads
# if __name__ == '__main__':
#     for t in driver.threads:
#         #print(t.getName())
#         t.start()
# 安卓配置文件
driver = driver
import time
# 登录判断
from min import log
# 加入会议
from mian import meetingAdd
# tryCatch
from selenium.common.exceptions import NoSuchElementException
# 点击
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
# 时间
import datetime



# 会议内操作
# 登录判断
try:
    if not driver.find_elements_by_id(
            "cn.redcdn.globalcare:id/title_txt"):
        print("")
    else:
        logTitle = driver.find_element_by_id(
            "cn.redcdn.globalcare:id/title_txt")
        log.logjudge(logTitle)
except NoSuchElementException:
    print("不存在重新登录！")

try:
    if driver.find_elements_by_id(
            "cn.redcdn.globalcare:id/qn_operae_dialog_right_button") and not driver.find_elements_by_id(
        "cn.redcdn.globalcare:id/rb_meeting"):
        print("存在加入会议提示框")
        driver.find_element_by_id("cn.redcdn.globalcare:id/qn_operae_dialog_right_button").click()
        meetingAdd.ad()
        # driver.find_element_by_id("cn.redcdn.globalcare:id/mic_state_iv").click()
    else:
        print("不存在加入会议提示框")
        meetingAdd.ad()

except NoSuchElementException:
    print("不存在加入会议提示框")

# 触及会议内屏幕
def touchscreen():
    time.sleep(2)
    # nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(nowTime)
    # 直接取消发言
    try:
        if not driver.find_elements_by_id("cn.redcdn.globalcare:id/top_menu") and not driver.find_elements_by_id(
                "cn.redcdn.globalcare:id/bottom_menu_view"):
            TouchAction(driver).tap(x=589, y=382).perform()
            driver.find_element_by_id("cn.redcdn.globalcare:id/meeting_room_menu_main_view_exit_btn").click()
        #elif driver.find_elements_by_id("cn.redcdn.globalcare:id/custom_dialog_bg"):
            driver.find_element_by_id("cn.redcdn.globalcare:id/host_right_button").click()

    except NoSuchElementException:
        print("报错")


# 检查是否存在取消发言再发言的弹框
i = 1
while True:
    # 判断是否存在取消发言再发言的弹框
    i += 1
    if not driver.find_elements_by_id("cn.redcdn.globalcare:id/rb_meeting"):
        touchscreen()
    else:
        try:
            if driver.find_elements_by_id(
                    "cn.redcdn.globalcare:id/qn_operae_dialog_right_button") and not driver.find_elements_by_id(
                "cn.redcdn.globalcare:id/rb_meeting"):
                print("存在加入会议提示框")
                driver.find_element_by_id("cn.redcdn.globalcare:id/qn_operae_dialog_right_button").click()
                meetingAdd.ad()
                # driver.find_element_by_id("cn.redcdn.globalcare:id/mic_state_iv").click()
            else:
                print("不存在加入会议提示框")
                meetingAdd.ad()

        except NoSuchElementException:
            print("不存在加入会议提示框")

        print(i)

    print(i)



# 底部菜单栏
# cn.redcdn.globalcare:id/bottom_menu_view

# 取消发言
# cn.redcdn.globalcare:id/speak_or_hand_btn

# 加入会议操作
# TouchAction(driver).tap(x=902, y=858).perform()
# TouchAction(driver).tap(x=665, y=2233).perform()
# TouchAction(driver).tap(x=615, y=535).perform()
# TouchAction(driver).tap(x=291, y=1713).perform()
# TouchAction(driver).tap(x=545, y=2222).perform()
# TouchAction(driver).tap(x=538, y=556).perform()
# TouchAction(driver).tap(x=484, y=673).perform()
# TouchAction(driver).tap(x=956, y=531).perform()
# TouchAction(driver).tap(x=1025, y=487).perform()
# TouchAction(driver).tap(x=709, y=789).perform()
# TouchAction(driver).tap(x=709, y=807).perform()
# TouchAction(driver).tap(x=1727, y=22).perform()
