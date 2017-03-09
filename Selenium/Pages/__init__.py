from HomePage import *
from RegisterPage import *
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

username = 'testSele'
password = '123456'
email = 'testSelenium@yahoo.com'

browser = webdriver.Chrome(executable_path='C:\Users\Three\AppData\Local\Google\Chrome\Application\chromedriver.exe')
url = 'http://www.millionairematch.com/?use_cdn=0'
browser.get(url)
browser.maximize_window()

browser.find_element_by_xpath()

time.sleep(2)
home = Homepage(browser)
browser.save_screenshot('E:\Study\Python\Three\Selenium\Pages\HomePage.png')
home.joinNow1().click()
time.sleep(2)
register = RegisterPage(browser)
register.firstname().send_keys('Deng')
register.username().send_keys(username)
register.password().send_keys(password)
register.email().send_keys(email)
register.age().send_keys('23')
Select(register.income()).select_by_index(4)
browser.save_screenshot('E:\Study\Python\Three\Selenium\Pages\Register1.png')
Select(register.ethnicity()).select_by_index(4)
Select(register.status()).select_by_index(4)
Select(register.height()).select_by_index(4)
register.gender1().click()
register.seeking1().click()
Select(register.country()).select_by_index(0)
register.zip().send_keys('10024')
register.check().click()
js="var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
browser.save_screenshot('E:\Study\Python\Three\Selenium\Pages\Register2.png')
time.sleep(3)
register.submit().click()

time.sleep(4)


