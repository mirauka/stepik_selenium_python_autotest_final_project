from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/login/" in self.browser.current_url, "Login url is incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS_LOGIN_TEXTFIELD)
        # self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN_TEXTFIELD)
        # self.is_element_present(*LoginPageLocators.LOGIN_BUTTON)
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # self.is_element_present(*LoginPageLocators, EMAIL_ADDRESS_REGISTER_TEXTFIELD)
        # self.is_element_present(*LoginPageLocators, PASSWORD_REGISTER_TEXTFIELD)
        # self.is_element_present(*LoginPageLocators, CONFIRM_PASSWORD_REGISTER_TEXTFIELD)
        # self.is_element_present(*LoginPageLocators, REGISTER_BUTTON)
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"