# -*- coding: utf-8 -*-#
import yaml
import sys
import os
from appium import webdriver
import time
import threading
import config.join_meeting,config.log_out,config.log_in,config.exit_meeting
import Include.log_main,Include.location_toast,Include.TurnOn_Camera_TurnOff,Include.Demo_login
import SDK.initialize_sdk,SDK.join_meeting_SDK,SDK.exit_meeting,SDK.operation_video,SDK.meeting_being,SDK.main_page_function

import HTMLTestRunner
#多进程工具包  与threading类似
import multiprocessing
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
import subprocess

def appium_start(port,udid):
    a = os.popen('netstat -ano | findstr "%s" ' % port)
    time.sleep(5)
    #print("执行5秒启动")
    t1 = a.read()
    if "LISTENING" in t1:
        print("appium服务已经启动：%s" % t1)
    else:
        #-U 是连接的设备名称，如"adb devices"获取的设备标识（也可写成--udid）
        os.system("start appium -a 127.0.0.1 -p %s -U %s --session-override" % (port, udid))
        # os.system("start appium -a 127.0.0.1 -p 4723 -U 192.168.1.109 --session-override")
        #cmd = 'start /b appium -a 127.0.0.1 -p '+str(port)+' -bp '+str(udid)
        #os.system("start appium -a 127.0.0.1 -p %s -U %s --no-reset --session-override" % (port, udid))
        #subprocess.Popen(cmd,shell=True)

    #print(1)
    # print(driver)
    #return driver
def dev_caps(deviceName):
    print(deviceName)
    driver_list = []
    curpath = os.path.dirname(os.path.realpath('__file__'))
    p = os.path.join(curpath, "红云会议_3.5.43.712.apk")
    with open('devicesYAML', "r",encoding="utf-8") as file:
        data = yaml.load(file, yaml.FullLoader)
    for i in data:
        if deviceName in i['dev']:
            appium_start(port=i['caps']['port'],udid=i['caps']['udid'])
            driver = webdriver.Remote('http://127.0.0.1:' + str(i['caps']['port']) + '/wd/hub',i['caps'])
            driver.implicitly_wait(10)
            time.sleep(10)


            #Include.log_main.run_app(deviceName,driver)
            try:
                print("START ACTION!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                #SDK.initialize_sdk.init(driver)
                #SDK.operation_video.close_video(driver)
                #会议内操作
                # SDK.join_meeting_SDK.Join_meeting(driver)

                # a = SDK.meeting_being.method()
                # a.open_video(driver)
                # a.close_video(driver)
                # a.close_voice(driver)
                # a.open_voice(driver)
                # a.share_desktop_open(driver)
                # a.share_desktop_close(driver)
                # a.share_whiteboard_open(driver)
                # a.share_whiteboard_close(driver)
                # a.meeting_list(driver)
                # a.meeting_list_openvideo(driver)
                # a.meeting_list_closevideo(driver)
                # a.meeting_list_openvoice(driver)
                # a.meeting_list_closevoice(driver)
                # a.meeting_list_raisehands(driver)
                # a.meeting_list_downhands(driver)
                # a.meeting_list_hide(driver)
                # a.raise_hands(driver)
                # a.down_hands(driver)
                #a.chat(driver)
                #SDK.exit_meeting.exit_meeting(driver)

                #会外设置水印
                #b = SDK.main_page_function.method()
                #b.watermark(driver)
                #SDK.join_meeting_SDK.Join_meeting(driver)
                Include.location_toast.laction_toast_Demo(driver)
                #Include.Demo_login.login_circulation(driver)
                #driver.find_element_by_id("cn.butel.redmeeting:id/head_iv").click()
                print("End ACTION!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            except Exception as e:
                print(e)




#devices_list = ['127.0.0.1:55560', '127.0.0.1:55570','127.0.0.1:55580']
#queueLock = threading.Lock()
# 构建线程组

class thread_m(threading.Thread):
    def __init__(self, target, args):
        threading.Thread.__init__(self)
        self.target = target
        self.args = args

#启动appium服务
# for i in range(len(devices_list)):
#     port = 4723 + 2 * i
#     print(devices_list)
#     f1 = threading.Thread(target=appium_start, args=(port,devices_list[i]))
#     f1.start()
#     f1.join()
#     print("启动成功！")

#启动设备
threads = []
#devices_name = ["华为mate30", "oppoA5", "华为9a"]
devices_name = ["华为9a"]

for j in range(len(devices_name)):
    t = threading.Thread(target=dev_caps, args=(devices_name[j],))
    threads.append(t)
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()

    print("执行已结束！！")
    # now_time = time.strftime("%Y%m%d_%H-%M-%S")
    # file_path = open('./test_report/_TestResult.html', 'wb')
    # runner = HTMLTestRunner(
    #     stream=file_path,  # 文件
    #     title='计算器测试报告',   # 标题
    #     description='测试用例执行情况',   # 副标题
    # )
    # runner.run(suite)
    # file_path.close()
