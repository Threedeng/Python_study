# coding = utf-8

from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='C:\Users\Three\AppData\Local\Google\Chrome\Application\chromedriver.exe')

url = 'http://www.millionairematch.com/?use_cdn=0'
browser.get(url)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="hp_center"]/ul[1]/li[4]/a/img').click()
print  'Now access ' + url
print 'Title:' + browser.title
browser.maximize_window()
time.sleep(2)
browser.back()
time.sleep(2)
browser.quit()
