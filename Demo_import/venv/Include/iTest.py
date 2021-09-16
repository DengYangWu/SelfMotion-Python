from selenium import webdriver
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import threading


# caps = {}
# caps["platformName"] = "Android"
# caps["platformVersion"] = "8.1.0"
# caps["deviceName"] = "192.168.1.115:5559"
# caps["appPackage"] = "cn.butel.redmeeting"
# caps["appActivity"] = "cn.butel.redmeeting.boot.SplashActivity"
# caps["noReset"] = "true"
# caps["udid"] = "192.168.1.115:5559"
# caps["automationName"] = "UiAutomator1"
# caps["skipServerInstallation"] = "true"
# caps["skipDeviceInitialization"] = "true"
# caps["newCommandTimeout"] = "600"
# cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
class TestUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有用例执行前执行")

    def setUp(self):
        print("每个用例开始前执行")

    def tearDown(self):
        print("每个用例结束后执行")

    @classmethod
    def tearDownClass(cls):
        print("所有用例执行后执行")

    def testA(self):
        '''用例A'''
        print("用例A执行了")
        self.assertEquals(1, 1)

    def testB(self):
        '''用例B'''
        print("用例B执行了")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
# class Test_Web_UI(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         #cls.driver = webdriver.Chrome()
#
#     @classmethod
#     def tearDownClass(cls):
#         pass
#
#     #case
#     def test_case01(self):
#         print("* 第 1 个用例 *")
#
#
#     def test_case02(self):
#         print("* 第 2 个用例 *")
#
#     def test_case03(self):
#         print("* 第 3 个用例 *")
#
# if __name__ == '__main__':
#     unittest.main()