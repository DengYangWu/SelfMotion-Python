# -*- coding: utf-8 -*-

import os
import sys
import re
import yaml
import sys
import os
from appium import webdriver
#driver = Include.Runner.dev_caps("华为9a")
#driver=webdriver.Remote("http://localhost:55580/wd/hub",desired_cups)
#获取屏幕机器大小x,y
def getSize(driver):
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return (x,y)

#屏幕向上滑动
def swipeup(t):
    print("正在向上滑动..")
    screensize=getSize()
    x1=int(screensize[0]*0.5)#x坐标
    y1=int(screensize[1]*0.75)#起始y坐标
    y2=int(screensize[1]*0.25)#终点y坐标
    driver.swipe(x1,y1,x1,y2,t)

#屏幕向下滑动
def swipedown(t):
    print("正在向下滑动...")
    screensize=getSize()
    x1=int(screensize[0]*0.5)#x坐标
    y1=int(screensize[1]*0.25)#起始y坐标
    y2=int(screensize[1]*0.75)#终点y坐标
    driver.swipe(x1,y1,x1,y2,t)

#屏幕向左滑动
def swipeleft(n,t):
    print("正在向左滑动...")
    screensize=getSize()
    x1=int(screensize[0]*0.9)
    y1=int(screensize[1]*0.5)
    x2=int(screensize[0]*0.1)
    for i in range(0,n):#for循环，控制滑动次数
        time.sleep(3)
        driver.swipe(x1,y1,x2,y1,t)
        print("成功向左滑动：",n,"次")

#屏幕向右滑动
def swiperight(n,t):
    print("正在向右滑动...")
    screensize=getSize()
    x1=int(screensize[0]*0.1)
    y1=int(screensize[1]*0.5)
    x2=int(screensize[0]*0.9)
    for i in range(0,n):
        time.sleep(3)
        driver.swipe(x1,y1,x2,y1,t)
        print("成功向右滑动：",n,"次")

# #调用向上滑动
# swipeup(1000)
#
# #调用向下滑动
# swipedown(1000)
#
# #调用向左滑动
# swipeleft(2,1000)
#
# #调用向右滑动
# swiperight(2,1000)