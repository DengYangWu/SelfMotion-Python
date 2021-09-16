from config import driver
driver = driver.driver

def logjudge(object):
    if object is None:
        print("直接进入app")
    else:
        driver.find_element_by_id("cn.redcdn.globalcare:id/login_login_btn").click()
        print("重新登录")
    return 0


