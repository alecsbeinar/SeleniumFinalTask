from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login part is missed in url\n"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented\n"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented\n"

    def register_new_user(self, email, password):
        inp_email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_REGISTER)
        inp_email.send_keys(email)
        inp_password = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_REGISTER)
        inp_password.send_keys(password)
        inp_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_REGISTER_REPEAT)
        inp_password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
