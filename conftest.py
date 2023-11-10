import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.add_argument('headless')    # данные опции запускают тесты без визуального отображения открытия браузера
    # options.add_argument('window-size=1920x935') #данные опции запускают тесты без визуального отображения открытия браузера
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
   # browser.implicitly_wait(15)
    #browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

