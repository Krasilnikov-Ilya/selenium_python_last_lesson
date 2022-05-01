from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUY_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    ITEM_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")