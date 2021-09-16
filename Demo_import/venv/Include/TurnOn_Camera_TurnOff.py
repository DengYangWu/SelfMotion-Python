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
#元素等待
from selenium.webdriver.support.ui import WebDriverWait

def camera_(driver):
    print("Open Camera")
