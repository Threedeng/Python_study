from selenium import webdriver

class RegisterPage:

    def __init__(self,browser):
        self.browser = browser

    def firstname(self):
        return self.browser.find_element_by_xpath('//*[@id="fname"]')

    def username(self):
        return self.browser.find_element_by_xpath('//*[@id="username"]')

    def password(self):
        return self.browser.find_element_by_xpath('//*[@id="password"]')

    def email(self):
        return self.browser.find_element_by_xpath('//*[@id="email"]')

    def age(self):
        return self.browser.find_element_by_xpath('//*[@id="age"]')

    def income(self):
        return self.browser.find_element_by_xpath('//*[@id="type"]')

    def ethnicity(self):
        return self.browser.find_element_by_xpath('//*[@id="ethnicity"]')

    def status(self):
        return self.browser.find_element_by_xpath('//*[@id="marital"]')

    def height(self):
        return self.browser.find_element_by_xpath('//*[@id="height_all"]')

    def gender1(self):
        return self.browser.find_element_by_xpath('//*[@id="gender.1"]')

    def seeking1(self):
        return self.browser.find_element_by_xpath('//*[@id="match_gender.2"]')

    def country(self):
        return self.browser.find_element_by_xpath('//*[@id="r_country"]')

    def zip(self):
        return self.browser.find_element_by_xpath('//*[@id="r_zip"]')

    def check(self):
        return self.browser.find_element_by_xpath('//*[@id="agree"]')

    def submit(self):
        return self.browser.find_element_by_xpath('//*[@id="continue"]')


