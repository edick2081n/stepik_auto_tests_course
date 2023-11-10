from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators



class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        self.url_suffix = ""


    def go_to_login_page(self):
        self.login_url.click()

    def should_be_login_link(self):
        #assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        self.check_login_link_present()




#   из урока  Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно
#   соответствующим образом с помощью self:        как это понять
# Как сравнить две записи функции  def should_be_login_link
# почему метод is_element_present выделяется