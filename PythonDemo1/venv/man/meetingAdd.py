from config import driver
driver = driver.driver
import time
# GUI
import easygui
#加入会议
def ad():
    print("会议")
    # meetingID = easygui.integerbox(msg="请输入要加入的会议号",title="会议号",lowerbound=10000000,upperbound=99999999)
    # print(int(meetingID))
    driver.find_element_by_id("cn.redcdn.globalcare:id/rb_meeting").click()
    # driver.find_element_by_id("cn.redcdn.globalcare:id/meetingid_input_edit").send_keys(meetingID)
    driver.find_element_by_id("cn.redcdn.globalcare:id/meetingid_input_edit").send_keys("90004757")
    driver.find_element_by_id("cn.redcdn.globalcare:id/meeting_consult_meetining_join_meeting").click()




# #点击会议视频屏幕
# def click_v():
#     print(5)
#
#     #driver.find_element_by_id("cn.redcdn.globalcare:id/fl_barrage").click()

# # 会议内动作
# # 会议内关闭mac
# def mac_close():
#     print("123")
#     driver.find_element_by_id("cn.redcdn.globalcare:id/mic_state_iv").click()
#     print("已关闭mac")