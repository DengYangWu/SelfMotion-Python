# -*- coding: utf-8 -*-#
import yaml
import sys
import os
from appium import webdriver
import unittest
import time
import yaml
import threading
import config.driver,config.Log_out,config.log_in

#多进程工具包  与threading类似
import multiprocessing
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

def appium_start(port,udid):
    a = os.popen('netstat -ano | findstr "%s" ' % port)
    #time.sleep(2)
    #print("执行5秒启动")
    t1 = a.read()
    if "LISTENING" in t1:
        print("appium服务已经启动：%s" % t1)
    else:
        #-U 是连接的设备名称，如"adb devices"获取的设备标识（也可写成--udid）
        os.system("start appium -a 127.0.0.1 -p %s -U %s --session-override" % (port, udid))

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
            try:
                time.sleep(5)
                if deviceName=="华为mate30":
                    if driver.find_elements_by_id("cn.butel.redmeeting:id/tv_content"):
                        driver.find_element_by_id("cn.butel.redmeeting:id/btn_left").click()
                        #退出登录
                        config.Log_out.log(driver)
                        # 登录操作
                        config.log_in.log_in_(driver,"18573440621","12345678Dyw")
                        #输入会议号-加入会议
                        config.driver.Join_meeting(driver)
                    elif not driver.find_elements_by_id("cn.butel.redmeeting:id/tv_content"):
                        if not driver.find_elements_by_id("cn.butel.redmeeting:id/head_iv"):
                            print("1_2_3")
                            print(driver)
                            config.log_in.log_in_(driver, "18573440621", "12345678Dyw")
                            config.driver.Join_meeting(driver)
                        else:
                            # 退出登录
                            config.Log_out.log(driver)
                            #登录操作
                            config.log_in.log_in_(driver, "18573440621", "12345678Dyw")
                            # 输入会议号-加入会议
                            config.driver.Join_meeting(driver)

                elif deviceName=="华为9a":
                    if driver.find_elements_by_id("cn.butel.redmeeting:id/tv_content"):
                        driver.find_element_by_id("cn.butel.redmeeting:id/btn_left").click()
                        # 退出登录
                        config.Log_out.log(driver)
                        # 登录操作
                        print(driver)
                        config.log_in.log_in_(driver, "15115450165", "12345678")
                        config.driver.Join_meeting(driver)

                    elif not driver.find_elements_by_id("cn.butel.redmeeting:id/tv_content"):
                        if not driver.find_elements_by_id("cn.butel.redmeeting:id/head_iv"):
                            # print("1_2_3")
                            print(driver)
                            config.log_in.log_in_(driver, "15115450165", "12345678")
                            config.driver.Join_meeting(driver)
                        else:
                            # 退出登录
                            config.Log_out.log(driver)
                            #登录操作
                            print(driver)
                            config.log_in.log_in_(driver, "15115450165", "12345678")
                            # 输入会议号-加入会议
                            config.driver.Join_meeting(driver)



                #自动登录 进入会议脚本
                # driver.find_element_by_id("cn.butel.redmeeting:id/join_meeting_ly").click()
                # driver.find_element_by_id("cn.butel.redmeeting:id/meetingid_input_edit").send_keys("10230995")
                # driver.find_element_by_id("cn.butel.redmeeting:id/join_meeting_btn").click()
            except Exception as e:
                print(e)
            #driver.implicitly_wait(10)
            #driver_list.append(driver)
            # strActivity = driver.current_activity
            #
            # if strActivity == ".boot.SplashActivity":
            # time.ctime(7)
            # print(driver.find_element_by_id('cn.butel.redmeeting:id/join_meeting_ly').size)
            # if driver.find_element_by_id('cn.butel.redmeeting:id/join_meeting_ly').size !=0:
            #     print("存在")
            # else:
            #     print("2没有元素")
            # print(321)
            #run_app(driver_list)
            #driver.quit()

def run_app(driver_list):
    # strActivity = driver.current_activity
    # print(strActivity)
    # if strActivity == ".boot.SplashActivity":
    #print(dev_caps())
    print("设备：")
    time.sleep(5)
    try:
        for driver in driver_list:
            # driver = webdriver.Remote(server, desired_caps)
            # driver.implicitly_wait(10)
            print(driver)
            #print(driver.findElement("cn.butel.redmeeting:id/join_meeting_ly").text)
            driver.find_element_by_id("cn.butel.redmeeting:id/join_meeting_ly").click()
            driver.find_element_by_id("cn.butel.redmeeting:id/meetingid_input_edit")
            print("执行到这一步")
    except Exception as e:
        print(e)
        # if driver.find_elements_by_id("cn.butel.redmeeting:id/join_meeting_ly"):
        #     print("存在")
        #     # try:
        #     #     driver.find_element_by_id("cn.butel.redmeeting:id/join_meeting_ly").click()
        #     # except NoSuchElementException:
        #     #     print("1没有元素")
        # else:
        #     print("2没有元素")

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
devices_name = ["华为mate30", "华为9a"]
for j in range(len(devices_name)):
    t = threading.Thread(target=dev_caps, args=(devices_name[j],))
    threads.append(t)
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()




