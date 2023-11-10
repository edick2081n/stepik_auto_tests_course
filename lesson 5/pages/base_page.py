import math
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from stere import Page
from stere.fields import Link
from .locators import MainPageLocators



class BasePage(Page):
    def __init__(self):

        # self.browser = browser
        # self.url = url
        self.login_url:Link = Link(*MainPageLocators)


    def open(self):
        self.navigate()

    def check_login_link_present(self):
        assert self.login_url.is_present()



    def solve_quiz_and_get_code(self):
        alert = self.browser.get_alert()
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()

        try:
            alert = self.browser.get_alert()
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()

        except NoAlertPresentException:
            print("No second alert presented")




