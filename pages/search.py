from data.locators import *
class search():
    def __init__(self,driver):
        self.driver = driver
    def search(self):
        self.driver.find_element_by_id(SEARCH_ID).send_keys(INPUT_VALUE)
        self.driver.find_element_by_class_name(CLASS_NAME).click()
        a = self.driver.find_element_by_xpath(ITEM_LOC)
        a.click()
        #print("done")
        #print("current window", driver.current_window_handle)
        cur_win = self.driver.current_window_handle
        win_hand = self.driver.window_handles
        #print(win_hand)
        for i in win_hand:
            if i!= cur_win :
                self.driver.switch_to.window(i)