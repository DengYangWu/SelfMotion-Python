import yaml
import os
from appium import webdriver
import unittest
import time
import yaml
import os
import threading

def log_in_(driver,account,password):
    driver.find_element_by_id("cn.butel.redmeeting:id/login_num_ed").send_keys(account)
    driver.find_element_by_id("cn.butel.redmeeting:id/login_pwd_ed").send_keys(password)
    driver.find_element_by_id("cn.butel.redmeeting:id/login_btn").click()