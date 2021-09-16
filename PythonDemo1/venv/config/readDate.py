import yaml
import os
from appium import webdriver
import unittest
import time
import yaml
import os
import threading


#启动appium端口服务
def start_appium_(port="",udid=""):
    a = os.popen('netstat -ano | findstr "%s" ' % port)
    time.sleep(2)
    t1 = a.read()
    if "LISTENING" in t1:
        print("appium服务已经启动：%s" % t1)
    else:
        #-U 是连接的设备名称，如"adb devices"获取的设备标识（也可写成--udid）
        os.system("start appium -a 127.0.0.1 -p %s -U %s --no-reset" % (port,udid))

#读取yaml文件，并判断是否连接appium服务成功
def android_driver(devicesName):
    curpath = os.path.dirname(os.path.realpath(__file__))

    yamlpath=os.path.join(curpath,'devicesYAML')
    #print(r'配置地址：%s' % yamlpath)
    f = open(yamlpath,"r",encoding="utf-8")
    a = f.read()
    f.close()
    #print(devicesName)
    #把yaml文件转字典
    d = yaml.load(a,Loader=yaml.FullLoader)
    #print(d)
    for i in d:
        if devicesName in i['dev']:
            start_appium_(port=i['caps']['port'],udid=i['caps']['udid'])
            return (i['caps'],i['caps']['port'],i['caps']['udid'])

# for i in devices:
#     run_app(devicesName=i)

def run_app(devicesName):
    curpath = os.path.dirname(os.path.realpath(__file__))
    p = os.path.join(curpath,"红云会议_3.5.43.706.apk")
    #配置参数
    caps = android_driver(devicesName)
    #执行代码
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % caps[1],caps[0])
    installSuccess = os.system("adb -s "+caps[2]+" install "+p)
    print(installSuccess)
    #time.sleep(4)
    print(4)
    if installSuccess == "":
        print("检测到安装")
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout").click()

    print(driver)
    # if driver:
    #     time.sleep(2)
    #     driver.find_element_by_id('cn.butel.redmeeting:id/join_meeting_ly').click()
    # time.sleep(2)
    # driver.find_element_by_id('cn.butel.redmeeting:id/join_meeting_ly').click()

    # driver.find_element_by_xpath("//*[@text='加入会议']").click()
    #return driver


    # def run(self):
    #     print ("开始线程：" + self.name)
    #     # print_time(self.name, self.counter, 5)
    #     print ("退出线程：" + self.name)
#多设备名称
devices_list = ['127.0.0.1:55560', '127.0.0.1:55570','127.0.0.1:55580']
threadList = ["华为mate30", "华为9a", "oppoA5"]
#threadList = ["oppoA5"]
queueLock = threading.Lock()

threads = []
class myThread (threading.Thread):
    def __init__(self, target, args):
        threading.Thread.__init__(self)
        self.target = target
        self.args = args

# 创建新线程
for i in range(len(threadList)):
    port = 4723 + 2 * i
    f1 = threading.Thread(target=android_driver, args=threadList[i])
    f1.start()
    f1.join()


# if __name__ == '__main__':
#     for t in threads:
#         t.join()
print ("退出主线程")

# threads = []
# t1 = threading.Thread(target=run_app,args=(u'华为mate30'.encode("utf-8"),))
# threads.append(t1)
# t2 = threading.Thread(target=run_app,args=(u'华为9a'.encode("utf-8")))
# threads.append(t2)
# t3 = threading.Thread(target=run_app,args=(u'oppoA5'.encode("utf-8")))
# threads.append(t3)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()



