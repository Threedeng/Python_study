#-*- coding=utf-8 -*-

def loginTabL(self):
    return self.driver.find_element_by_class_name('login-tab-l')

def loginTabR(self):
    return self.driver.find_element_by_class_name('login-tab-r')

def username(self):
    return self.driver.find_element_by_id('loginname')

def password(self):
    return self.driver.find_element_by_id('nloginpwd')

def loginSubmit(self):
    return self.driver.find_element_by_id('loginsubmit')

def forgotPWD(self):
    return self.driver.find_element_by_class_name('forget-pw-safe')

