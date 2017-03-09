from selenium import webdriver

class Homepage:

    def __init__(self,browser):
        self.browser = browser

    def joinNow1(self):
        return self.browser.find_element_by_xpath('//*[@id="hp_center"]/ul[1]/li[3]/a/img')
