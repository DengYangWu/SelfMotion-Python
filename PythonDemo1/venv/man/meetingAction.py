from config import driver
driver = driver.driver
from appium.webdriver.common.touch_action import TouchAction
# 会议内动作
# 退出会议
def exit_meeting():
    if not driver.find_elements_by_id("cn.redcdn.globalcare:id/meeting_room_menu_main_view_exit_btn"):
        TouchAction(driver).tap(x=589, y=382).perform()
        # cn.redcdn.globalcare:id/host_right_button  退出会议id
        # cn.redcdn.globalcare:id/qn_operate_dialog_body_parent 退出会议提示框
        # cn.redcdn.globalcare:id/host_middle_button 结束会议id
        driver.find_element_by_id("cn.redcdn.globalcare:id/meeting_room_menu_main_view_exit_btn").click()
        driver.find_element_by_id("cn.redcdn.globalcare:id/host_right_button").click()
    else:
        driver.find_element_by_id("cn.redcdn.globalcare:id/meeting_room_menu_main_view_exit_btn").click()
        driver.find_element_by_id("cn.redcdn.globalcare:id/host_right_button").click()


