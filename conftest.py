import pytest

@pytest.fixture(scope="class")

def webcontrol (request):
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Users/AMUL JADHAV/PycharmProjects/amazon/drivers/chromedriver.exe")
    driver.get("https://www.amazon.in/")
    driver.implicitly_wait(15)
    driver.maximize_window()
    request.cls.driver = driver
