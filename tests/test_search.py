import pytest
from pages.search import search
from pages.addtocart import addtocart
from pages.pay import pay
@pytest.mark.usefixtures("webcontrol")
class Test_amazon:
    def test_search(self):
        driver = self.driver
        se = search(driver)
        se.search()

    def test_addtocart(self):
        driver = self.driver
        add = addtocart(driver)
        add.addtocart()

    def test_pay(self):
     driver = self.driver
     payment = pay(driver)
     payment.pay()

