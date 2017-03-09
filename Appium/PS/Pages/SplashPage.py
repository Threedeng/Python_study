#!E:\Study\Python\Appium\PS\Demo.py
# -*- coding: UTF-8 -*-
import  time
waittime = 1
pakacage = 'com.bana.dating'
class SplashPage:
    def __init__(self,driver):
        self.driver = driver
        self.driver.wait_activity(pakacage + '.splash.activity.SplashActivity',10,1)
        time.sleep(waittime)

    def clickOnLogin(self):
        self.driver.find_element_by_id('btnLogin').click()

    def clickOnRegister(self):
        self.driver.find_element_by_id('btnRegister').click()

    def scrollRight(self):
        print 'Please waiting for develop.'

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()