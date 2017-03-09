#!E:\Study\Python\Appium\PS\Demo.py
# -*- coding: UTF-8 -*-
import  time
waittime = 1
pakacage = 'com.bana.dating'

class Register1Page:
    def __init__(self, driver):
        self.driver = driver
#        self.driver.wait_activity(pakacage + '.usercenter.activity.RegisterActivity',2,1)
        time.sleep(waittime)

    def clickBackBt(self):
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()

    def inputEmail(self,email):
        self.driver.find_element_by_id('edittext_email').send_keys(email)

    def inputUsername(self,username):
        self.driver.find_element_by_id('edittext_username').send_keys(username)

    def inputPassword(self,password):
        self.driver.find_element_by_id('edittext_password').send_keys(password)

    def clickOnDone(self):
        self.driver.find_element_by_id('register_third_confirm_btn').click()

    def clickOnServiceAgreement(self):
        self.driver.find_element_by_id('Service_agreement').click()

    def clickOnPrivacyPolicy(self):
        self.driver.find_element_by_id('Privacy_policy').click()