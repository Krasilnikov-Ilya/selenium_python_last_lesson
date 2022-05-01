from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .login_page import LoginPage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        buy_button = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        buy_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_item_name_match(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_item_name = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert (item_name == added_item_name), "name does not match"

    def should_item_price_match(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        added_item_price = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_PRICE).text
        assert (item_price == added_item_price), "name does not match"