from .base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_page(self):
        def should_be_login_url(self):
            assert (LoginPageLocators.LOGIN_URL) in (driver.current_url), "Login link is incorrect"
        def should_be_login_form(self):
            assert self.browser.find_elements(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        def should_be_register_form(self):
            assert self.browser.find_elements(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"