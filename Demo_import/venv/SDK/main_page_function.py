import time
#import Include.Runner
from selenium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from Include import Runner

time.sleep(5)
class method():
    def watermark(self,driver):
        driver.find_element_by_id("demo.com.butel.redmeeting:id/water_mark_rl").click()
        print("设置文字水印")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/text_content_ed").send_keys("我是水印文字君~~~~~")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/text_type_ed").send_keys("微软雅黑")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/text_size_ed").send_keys(30)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/text_color_ed").send_keys(2516711680)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/text_bg_color_ed").send_keys(2516711935)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/text_position_ed").send_keys(0)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/text_position_x_ed").send_keys(20)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/text_position_y_ed").send_keys(30)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/watermark_text_switch").click()
        TouchAction(driver).press(x=45, y=1000).move_to(x=0, y=400).release().perform()
        time.sleep(3)
        print("设置时间水印")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/watermark_time_switch").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/time_type_ed").send_keys("微软雅黑")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/time_size_ed").send_keys(30)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/time_color_ed").send_keys(2516711680)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/time_bg_color_ed").send_keys(2516711935)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/time_position_ed").send_keys(1)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/time_position_x_ed").send_keys(20)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/time_position_y_ed").send_keys(30)
        TouchAction(driver).press(x=45, y=1000).move_to(x=0, y=400).release().perform()
        time.sleep(3)
        print("设置图片水印")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/image_position_ed").send_keys(3)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/image_position_x_ed").send_keys(20)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/image_position_y_ed").send_keys(10)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/image_transparency_ed").send_keys(200)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/image_zoom_ed").send_keys(5)
        driver.find_element_by_id("demo.com.butel.redmeeting:id/watermark_img").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/carema_rl").click()
        driver.find_element_by_id("com.huawei.camera:id/shutter_button").click()
        driver.find_element_by_id("com.huawei.camera:id/done_button").click()
        driver.find_element_by_id("demo.com.butel.redmeeting:id/watermark_img_switch").click()
        print("设置完毕，退出页面")
        driver.find_element_by_id("demo.com.butel.redmeeting:id/back_img").click()




