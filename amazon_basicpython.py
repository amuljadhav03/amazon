from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/AMUL JADHAV/PycharmProjects/amazon/drivers/chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.implicitly_wait(15)
driver.maximize_window()
driver.find_element_by_id("twotabsearchtextbox").send_keys("fossil nate analog black dial unisex watches")
driver.find_element_by_class_name("nav-input").click()
a = driver.find_element_by_xpath("//img [@src='https://m.media-amazon.com/images/I/81Juno1hkBL._AC_UL320_.jpg']")
a.click()
#print("done")
#print("current window", driver.current_window_handle)
cur_win = driver.current_window_handle
win_hand = driver.window_handles
#print(win_hand)
for i in win_hand:
    if i!= cur_win :
        driver.switch_to.window(i)
driver.find_element_by_id("add-to-cart-button").click()
driver.find_element_by_id("hlb-ptc-btn-native").click()