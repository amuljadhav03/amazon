from data.locators import *
class pay:
    def __init__(self,driver):
        self.driver = driver
    def pay(self):
        self.driver.find_element_by_id(PAYID).click()