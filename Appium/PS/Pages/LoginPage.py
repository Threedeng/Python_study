#!E:\Study\Python\Appium\PS\Demo.py
# -*- coding: UTF-8 -*-
import time
waittime = 1
pakacage = 'com.bana.dating'
class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.driver.wait_activity(pakacage + '.usercenter.activity.LoginActivity',10,1)
        time.sleep(waittime)

    def clickBackBt(self):
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()

    def inputUsername(self,username):
        self.driver.find_element_by_id('etLoginAccount').send_keys(username)

    def inputPassword(self,password):
        self.driver.find_element_by_id('etLoginPassword').send_keys(password)

    def clickForgotpassword(self):
        self.driver.find_element_by_id('tvForgotPassword').click()

    def clickSignIn(self):
        self.driver.find_element_by_id('btnLogin').click()

    def clickSignUp(self):
        self.driver.find_element_by_id('btnSignup').click()
