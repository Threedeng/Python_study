import  time
waittime = 1
pakacage = 'com.bana.dating'

class BrowsePage:
    def __init__(self, driver):
        self.driver = driver
#        self.driver.wait_activity(pakacage + '.usercenter.activity.RegisterActivity',2,1)
        time.sleep(waittime)

    def clickMenuBt(self):
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()

    def