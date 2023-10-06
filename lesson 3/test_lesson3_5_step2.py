import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


#   from selenium.webdriver.chrome.options import Options
#   from webdriver_manager.chrome import ChromeDriverManager
#   from selenium.webdriver.chrome.service import Service
#

#   options = Options()
#   options.add_argument("--ignore-certificate-errors")
#   options.add_experimental_option("excludeSwitches", ["enable-logging"])
#   browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# Данный код необходим для устранения ошибки с сертификатом