import time
#import Include.Runner
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from Include import Runner

time.sleep(5)
class method():
    def open_video(self,driver):
        print("打开摄像头")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/camera_hint").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/header_tool_view_meetingid_tv").click()


    def close_video(self,driver):
        print("关闭摄像头")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/camera_hint").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/header_tool_view_meetingid_tv").click()

    def open_voice(self,driver):
        print("打开语音")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/mic_hint").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/header_tool_view_meetingid_tv").click()


    def close_voice(self,driver):
        print("关闭语音")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/mic_hint").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/header_tool_view_meetingid_tv").click()

    def share_desktop_open(self,driver):
        print("打开共享屏幕")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/share_hint").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/screen_share_tv").click()
        driver.find_element_by_id("android:id/button1").click()

        # ele = driver.find_element_by_id("demo.com.butel.redmeeting:id/landscape_text")
        # if ele.is_displayed()==True:
        #     print("共享屏幕成功")
        # else:
        #     print("共享屏幕失败")
        #driver.find_element_by_id("demo.com.butel.redmeeting:id/header_tool_view_meetingid_tv").click()

    def share_desktop_close(self,driver):
        print("关闭共享屏幕")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/landscape_text").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/share_hint").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/btn_right").click()


    def share_whiteboard_open(self,driver):
        print("打开白板")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/share_hint").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/white_share_tv").click()

        # ele = driver.find_element_by_id("demo.com.butel.redmeeting:id/paint_lyt")
        # if ele.is_displayed()==True:
        #     print("共享白板成功")
        # else:
        #     print("共享白板失败")

    def share_whiteboard_close(self,driver):
        print("关闭白板")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/finish_btn").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/btn_right").click()

    def meeting_list(self,driver):
        print("参会列表按钮")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/member_hint").click()

    def meeting_list_openvoice(self,driver):
        print("参会列表操作打开麦克风")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_master_brief").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_mute_operation").click()
    def meeting_list_closevoice(self,driver):
        print("参会列表操作关闭麦克风")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_master_brief").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_mute_operation").click()
    def meeting_list_openvideo(self,driver):
        print("参会列表操作打开摄像头")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_master_brief").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_video_operation").click()
    def meeting_list_closevideo(self,driver):
        print("参会列表操作关闭摄像头")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_master_brief").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_video_operation").click()
    def meeting_list_raisehands(self,driver):
        print("参会列表操作举手")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_master_brief").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_hands_operation").click()
    def meeting_list_downhands(self,driver):
        print("参会列表操作放下手")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_master_brief").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_hands_operation").click()
    def meeting_list_hide(self,driver):
        print("参会列表按钮收起")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()

    def raise_hands(self,driver):
        print("举手")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_more").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/meeting_raisehand_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/header_tool_view_meetingid_tv").click()

    def down_hands(self,driver):
        print("放下手")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_more").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/meeting_raisehand_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/header_tool_view_meetingid_tv").click()

    def invite(self,driver):
        print("邀请")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/meeting_invite_tv").click()

    def chat(self,driver):
        print("聊天")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/speaker_name_tv").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_more").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/meeting_im_chat").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_send_msg_tip").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/tv_send_msg_tip").send_keys("hello??")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/btn_send").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/header_tool_view_meetingid_tv").click()

    def switch_screen_mode(self,driver):
        print("切换画面模式")


