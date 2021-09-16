import os
import threading
import multiprocessing
from appium import webdriver
class ConcurrentExecution:
    def __init__(self):
        self.driver_port = [[55560,"192.168.1.107:5556"],[55580,"192.168.1.100:5557"],[55570,"192.168.1.113:5558"]]

    def android_driver(self,i):
        driver_list = []
        capabilities = {
            "platformName" : "Android",
            "appPackage": "cn.butel.redmeeting",
            "appActivity": "cn.butel.redmeeting.boot.SplashActivity",
            "udid": self.driver_port[i][1],
            "deviceName": self.driver_port[i][1],
            "noReset": "True",
            "skipServerInstallation": "True",
            "skipDeviceInitialization": "True"
            }
        driver = webdriver.Remote("http://127.0.0.1:{0}/wd/hub".format(self.driver_port[i][0]),capabilities)
        driver_list.append(driver)
        return driver_list

    def kill_server(self):
        server_list = os.popen('tasklist | find "node.exe"').readlines()
        print(server_list)
        if len(server_list)>0:
            os.system("taskkill -F -PID node.exe")

    def start_appium_server(self,j):
        li_port = [55560,55570,55580]
        os.system("appium -p {0}".format(li_port[j]))

if __name__ == '__main__':
     obj = ConcurrentExecution()
     obj.kill_server()
     for j in range(3):  #启动服务
        th = threading.Thread(target=obj.start_appium_server,args=(j,))
        th.start()
     for i in range(3): #运行
        t = multiprocessing.Process(target=obj.android_driver,args=(i,))
        t.start()