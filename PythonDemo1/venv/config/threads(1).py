import os
import threading
from time import sleep
from time import ctime


def run_app(devicesName):
    print(devicesName)

class myThread (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    # def run(self):
    #     print ("开始线程：" + self.name)
    #     # print_time(self.name, self.counter, 5)
    #     print ("退出线程：" + self.name)

threadList = ["华为mate30", "华为9a", "oppoA5"]
queueLock = threading.Lock()

threads = []
# 创建新线程
for tName in threadList:
    t1 = myThread(run_app(tName))
    t1.start()
    threads.append(t1)


if __name__ == '__main__':
    for t in threads:
        t.join()
print ("退出主线程")


