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

    def clickBirthday(self):
        self.driver.find_element_by_id('register_second_my_age_parent').click()

    def clickEthnicity(self):
        self.driver.find_element_by_id('register_second_ethnicity_parent').click()

    def clickLivingWith(self):
        self.driver.find_element_by_id('register_second_living_with_parent').click()

    def clickLocation(self):
        self.driver.find_element_by_id('register_second_region_parent').click()

    def clickOnContinue(self):
        self.driver.find_element_by_id('register_second_confirm_btn').click()

    def selectEthnicityAsian(self):
        self.driver.find_element_by_name('Asian').click()

    def selectHIV(self):
        self.driver.find_element_by_name('HIV').click()

    def clickOnDone(self):
        time.sleep(waittime)
        self.driver.find_element_by_id('dialog_btn_done').click()

    def isFailedLocate(self):
        return self.driver.find_element_by_name('Failed to get your current location.').is_displayed()

    def clickOnSelectManually(self):
        self.driver.find_element_by_name('Select manually').click()







