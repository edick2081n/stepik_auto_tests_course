from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.url_suffix = "en-gb/accounts/login/"


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        a = self.browser.current_url
        assert "login" in a, "Login form url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER_NAME), "Login form username is not presented"
        assert self.is_element_present(*LoginPageLocators.lOGIN_USER_PASSWORD, "#id_login-password"), "Login form password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_NAME, "#id_registration-email"), "registration form username is not presented"
        assert self.is_element_present(*LoginPageLocators.lOGIN_USER_PASSWORD, "#id_registration-password1"), "registration form password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT, "#id_registration-password2"), "registration form repeat password is not presented"




