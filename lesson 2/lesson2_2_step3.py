# Задание: работа с выпадающим списком
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
# import warnings
#
# warnings.filterwarnings("ignore", category=DeprecationWarning)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])



try:
    link = " https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, "option")
    for element in elements:
        x = element.get_attribute("value")
        print(x)
        pass
    print(elements)
    # first_number = browser.find_element(By.CSS_SELECTOR, "#num1").text
    # second_number = browser.find_element(By.CSS_SELECTOR, "#num2").text
    # first_number = int(first_number)
    # second_number = int(second_number)
    # sum_numbers = sum([first_number, second_number])
    # # sum_numbers = str(sum_numbers)
    # # print(sum_numbers)
    # input1 = browser.find_element(By.CSS_SELECTOR, f"[value='{sum_numbers}']").click()
    # # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # # select.select_by_value("sum_numbers")
    #
    #
    #
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()
    #

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

