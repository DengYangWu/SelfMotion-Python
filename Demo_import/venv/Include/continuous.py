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
def tap_el(self, element, times: int):
    """
    单击某个控件N次
    :param element: 要单击的控件
    :param times: 要单击的次数
    :return:
    """
    def _center_rect(r):
        center_x = r['width'] / 2.0
        center_y = r['height'] / 2.0
        return center_x, center_y

    action = TouchAction(self)
    center = _center_rect(element.rect)
    action.tap(element=element,
               x=center[0],
               y=center[1],
               count=times).perform()