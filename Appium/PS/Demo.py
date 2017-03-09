#!E:\Study\Python\Appium\PS\Demo.py
# -*- coding: UTF-8 -*-
from Pages import *
from appium import webdriver
import time

class Demo:
    desired_caps = {}

    def __init__(self):
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '6.0.1'
        self.desired_caps['deviceName'] = 'MI 4LTE'
        self.desired_caps['appPackage'] = 'com.stddating.positivesingles'
        self.desired_caps['appActivity'] = '.activity.DispatcherActivity'


    def run(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        splash = SplashPage.SplashPage(self.driver)
        splash.clickOnLogin()
        login = LoginPage.LoginPage(self.driver)
        login.clickSignIn()
        login.inputUsername('123456')
        self.driver.deactivate_ime_engine()
        login.clickBackBt()
        splash.clickOnRegister()
        register1 = Register1Page.Register1Page(self.driver)
        register1.clickOnIam()
        register1.selectMan()
        register1.clickOnLookfor()
        register1.selectWoman()
        register1.clickOnContinue1()
        register2 = Register2Page.Register1Page(self.driver)
        register2.clickBirthday()
        register2.clickOnDone()
        register2.clickEthnicity()
        register2.selectEthnicityAsian()
        register2.clickLivingWith()
        register2.selectHIV()
        register2.clickOnDone()
        register2.clickLocation()
        while True:
            if (register2.isFailedLocate()):
                register2.clickOnSelectManually()

        time.sleep(2)
        self.driver.reset()
        self.driver.close_app()
        self.driver.quit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

