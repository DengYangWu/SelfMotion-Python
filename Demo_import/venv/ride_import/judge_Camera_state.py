#conding=utf-8
import yaml
import sys
import os
from appium import webdriver
import time
import yaml
import threading
import multiprocessing
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

def CameraState(state):
    
    print(state)