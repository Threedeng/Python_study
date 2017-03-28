from Pages import PageHome,PageLogin
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

username = '13086657448'
password = 'Deng8155195'

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Users\Three\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        self.url = 'https://www.jd.com/'
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_JD_login(self):
        driver = self.driver
        PageHome.toplogin(self).click()
        PageLogin.loginTabR(self).click()
        driver.back()
        driver.forward()
        PageLogin.loginTabR(self).click()
        PageLogin.username(self).clear()
        PageLogin.username(self).send_keys(username)
        PageLogin.password(self).clear()
        PageLogin.password(self).send_keys(password)
        time.sleep(2)
        PageLogin.loginSubmit(self).click()
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)




