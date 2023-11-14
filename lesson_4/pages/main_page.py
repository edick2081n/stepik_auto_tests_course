from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators



class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"





#   из урока  Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно
#   соответствующим образом с помощью self:        как это понять
# Как сравнить две записи функции  def should_be_login_link
# почему метод is_element_present выделяется