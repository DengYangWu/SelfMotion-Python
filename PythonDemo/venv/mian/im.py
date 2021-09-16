# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python


from config import driver

# 安卓配置文件
driver = driver.driver
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

# 判断是否存在加入会议的提示框
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


# except Exception as e:
#     print(str(e));

# 触及会议内屏幕
def touchscreen():
    time.sleep(2)
    # nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(nowTime)
    # 直接取消发言

    # if not driver.find_elements_by_id("cn.redcdn.globalcare:id/bottom_menu_view"):
    # print("直接取消发言")
    # TouchAction(driver).tap(x=334, y=368).perform()
    # TouchAction(driver).tap(x=769, y=821).perform()
    # time.sleep(2)
    # [921, 955][1006, 1077]
    # [929,955][998,1077]
    # s = driver.find_element_by_id("cn.redcdn.globalcare:id/speak_or_hand_tv").text
    # print(s)
    # time.sleep(2)
    # driver.find_element_by_id("cn.redcdn.globalcare:id/mic_change_layout").click()
    # driver.find_element_by_id("cn.redcdn.globalcare:id/camera_change_layout").click()
    # driver.find_element_by_id("cn.redcdn.globalcare:id/speak_or_hand_tv").click()
    # if s == "取消发言":
    #     TouchAction(driver).tap(x=910, y=950).perform()
    # else:
    #     TouchAction(driver).tap(x=998, y=1077).perform()
    # cn.redcdn.globalcare:id/speak_or_hand_btn
    # cn.redcdn.globalcare:id/menu_parent_layout
    # cn.redcdn.globalcare:id/fl_barrage

    # / hierarchy / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.FrameLayout / \
    #   android.widget.FrameLayout[2] / android.view.ViewGroup
    # cn.redcdn.globalcare:id/meeting_room_menu_main_view_ask_for_speak_btn 取消发言
    # cn.redcdn.globalcare:id/speak_or_hand_btn

    # if driver.find_elements_by_id(
    #         "cn.redcdn.globalcare:id/meeting_room_menu_ask_for_stop_speak_view_stop_speak_btn"):
    #     print("出现了取消发言弹框")
    #     driver.find_element_by_id(
    #         "cn.redcdn.globalcare:id/meeting_room_menu_ask_for_stop_speak_view_stop_speak_btn").click()
    try:
        if not driver.find_elements_by_id("cn.redcdn.globalcare:id/menuBg") and not driver.find_elements_by_id(
                "cn.redcdn.globalcare:id/bottom_menu_view"):
            TouchAction(driver).tap(x=589, y=382).perform()
            driver.find_element_by_id("cn.redcdn.globalcare:id/meeting_room_menu_main_view_participator_btn").click()
            driver.find_element_by_id("cn.redcdn.globalcare:id/meeting_room_menu_set_speaker_btn").click()
            #cn.redcdn.globalcare:id/userListView
            #x = driver.find_element_by_id("cn.redcdn.globalcare:id/userListView").tag_name
            e = driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.view.ViewGroup")
            # for e in range(x):
            #     print(x)
            #/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.view.ViewGroup[x]/android.widget.TextView[2]
            # for l[e] in ex:
            #     print(ex)

            # print("参会方列表不存在")
            # if driver.find_elements_by_id(
            #         "cn.redcdn.globalcare:id/meeting_room_menu_ask_for_stop_speak_view_stop_speak_btn"):
            #     print("出现了取消发言弹框")
            #     driver.find_element_by_id(
            #         "cn.redcdn.globalcare:id/meeting_room_menu_ask_for_stop_speak_view_stop_speak_btn").click()


        elif driver.find_elements_by_id("cn.redcdn.globalcare:id/menuBg"):


            driver.find_element_by_id("cn.redcdn.globalcare:id/meeting_room_menu_set_speaker_btn").click()

            print("参会方列表还存在")

            time.sleep(2)
            driver.find_element_by_id("cn.redcdn.globalcare:id/meeting_room_menu_main_view_ask_for_speak_btn").click()

    except NoSuchElementException:
        print("报错")


# 检查是否存在取消发言再发言的弹框
i = 1
while True:
    # 判断是否存在取消发言再发言的弹框
    i += 1
    if driver.find_elements_by_id("cn.redcdn.globalcare:id/qn_operae_dialog_left_button"):
        driver.find_element_by_id("cn.redcdn.globalcare:id/qn_operae_dialog_left_button").click()
        touchscreen()
    else:
        touchscreen()
    print(i)

print("死循环有出来吗")

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
