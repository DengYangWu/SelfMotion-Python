import threading

class With_thread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)

    def run(self):
        self._target(*self._args)

def some_Func(data, key):
    print("some_Func was called : data=%s; key=%s" % (str(data), str(key)))

f1 = With_thread(some_Func, [1,2], 6)
f1.start()
f1.join()

f2 = Without_thread(some_Func, [1,2], 6)
f2.foo()