#coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'MI 4LTE'
desired_caps['appPackage'] = 'com.stddating.positivesingles'
desired_caps['appActivity'] = '.activity.DispatcherActivity'
#desired_caps['waitappActivity'] = 'com.bana.dating.splash.activity.SplashActivity'
driver = webdriver.Remote
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print driver
time.sleep(2)
driver.find_element_by_id('btnLogin').click()
driver.quit()

'''
driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("delete").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()
'''

