# -*- coding: utf-8 -*-#
import yaml
import sys
import os
from appium import webdriver
import time
import yaml
import threading
import config.join_meeting,config.log_out,config.log_in,config.exit_meeting

import HTMLTestRunner
#多进程工具包  与threading类似
import multiprocessing
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction


def run_app(deviceName,driver):

    print("设备：%s"% deviceName)
    time.sleep(5)
    try:
        if deviceName == "华为mate30":
            #print(driverName)
            if driver.find_elements_by_id("cn.butel.redmeeting:id/tv_content"):
                driver.find_element_by_id("cn.butel.redmeeting:id/btn_left").click()
                # 退出登录
                config.log_out.log(driver)
                # 登录操作
                config.log_in.log_in_(driver, "15380900025", "12345678Dyw")
                # 输入会议号-加入会议
                config.join_meeting.Join_meeting(driver)
                #退出会议
                #config.exit_meeting.exit(driver)

            elif not driver.find_elements_by_id("cn.butel.redmeeting:id/tv_content"):
                #检测没有自动到主页
                if not driver.find_elements_by_id("cn.butel.redmeeting:id/head_iv"):
                    #登录
                    config.log_in.log_in_(driver, "15380900025", "12345678DywDyw")
                    #加入会议
                    config.join_meeting.Join_meeting(driver)
                    # 退出会议
                    #config.exit_meeting.exit(driver)

                else:
                    # 退出登录
                    config.log_out.log(driver)
                    # 登录操作
                    config.log_in.log_in_(driver, "15380900025", "12345678Dyw")
                    # 输入会议号-加入会议
                    config.join_meeting.Join_meeting(driver)
                    # 退出会议
                    #config.exit_meeting.exit(driver)

        elif deviceName == "华为9a":
            #检测存在退出会议弹框提示
            if driver.find_elements_by_id("cn.butel.redmeeting:id/tv_content"):
                #点击退出会议弹框提示“取消”
                driver.find_element_by_id("cn.butel.redmeeting:id/btn_left").click()
                # 退出登录
                config.log_out.log(driver)
                # 登录操作
                config.log_in.log_in_(driver, "18573440621", "12345678Dyw")
                #加入会议
                config.join_meeting.Join_meeting(driver)
                #退出会议
                #config.exit_meeting.exit(driver)

            elif not driver.find_elements_by_id("cn.butel.redmeeting:id/tv_content"):
                if not driver.find_elements_by_id("cn.butel.redmeeting:id/head_iv"):
                    #登录
                    config.log_in.log_in_(driver, "18573440621", "12345678Dyw")
                    #加入会议
                    config.join_meeting.Join_meeting(driver)
                    # 退出会议
                    #config.exit_meeting.exit(driver)
                else:
                    # 退出登录
                    config.log_out.log(driver)
                    # 登录操作
                    config.log_in.log_in_(driver, "18573440621", "12345678Dyw")
                    # 输入会议号-加入会议
                    config.join_meeting.Join_meeting(driver)
                    # 退出会议
                    #config.exit_meeting.exit(driver)

    except Exception as e:
        print(e)