#!E:\Study\Python\Appium\PS\Demo.py
# -*- coding: UTF-8 -*-
import  time
waittime = 1
pakacage = 'com.bana.dating'

class Register1Page:
    def __init__(self, driver):
        self.driver = driver
#        self.driver.wait_activity(pakacage + '.usercenter.activity.RegisterActivityr',2,1)
        time.sleep(waittime)

    def clickBackBt(self):
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()

    def clickOnIam(self):
        self.driver.find_element_by_id('register_first_i_am_a_parent').click()

    def clickOnLookfor(self):
        self.driver.find_element_by_id('register_first_looking_for_parent').click()

    def clickOnAges(self):
        self.driver.find_element_by_id('register_first_age_parent').click()

    def clickOnContinue1(self):
        self.driver.find_element_by_id('register_first_confirm_btn').click()

    def selectMan(self):
        self.driver.find_element_by_name('Man').click()

    def selectWoman(self):
        self.driver.find_element_by_name('Woman').click()

    def selectCouple(self):
        self.driver.find_element_by_name('Couple').click()

