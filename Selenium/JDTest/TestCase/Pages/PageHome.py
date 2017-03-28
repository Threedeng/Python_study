
def test():
    print 'I am Page Home Test'
def toplogin(self):
    return self.driver.find_element_by_class_name('link-login')

def infologin(self):
    return self.driver.find_element_by_class_name('user_info_login')

def topreg(self):
    return self.driver.find_element_by_class_name('link-regist')

def inforeg(self):
    return self.driver.find_element_by_class_name('user_info_reg')

def area(self):
    return self.driver.find_element_by_class_name('ui-areamini-text-wrap')

def charea(self, dataid):
    return self.driver.find_element_by_xpath('//*[@id="ttbar-mycity"]/div[2]/div[2]/div/div//a[@data-id="'+ dataid + '"]')