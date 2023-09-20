#Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = " https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    # скрипт для прокрутки страницы вниз

   #  input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
   # # browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
   #  input2.click()
   #  input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
   # # browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
   #  input3.click()
   #
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

