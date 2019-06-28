from data.locators import *
class addtocart:
    def __init__(self,driver):
        self.driver = driver
    def addtocart(self):
        self.driver.find_element_by_id(ADDTOID).click()