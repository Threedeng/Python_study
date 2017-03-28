import unittest
from selenium import webdriver
import time
from Pages import PageHome
from selenium.webdriver.common.action_chains import ActionChains

class ChArea(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Users\Three\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        self.url = 'https://www.jd.com/'
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_charea(self):
        driver =  self.driver
        ActionChains(driver).move_to_element(PageHome.area(self)).perform()
        cityid = 4
        PageHome.charea(self,dataid=str(cityid)).click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

