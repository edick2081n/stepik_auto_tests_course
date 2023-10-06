# Задание: работа с выпадающим списком
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = " https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    first_number = browser.find_element(By.CSS_SELECTOR, "#num1").text
    second_number = browser.find_element(By.CSS_SELECTOR, "#num2").text
    first_number = int(first_number)
    second_number = int(second_number)
    sum_numbers = sum([first_number, second_number])
    sum_numbers = str(sum_numbers)

    input1 = browser.find_element(By.CSS_SELECTOR, f"[value='{sum_numbers}']")
    input1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

