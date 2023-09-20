# Метод execute_script
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = " https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
   # browser.execute_script("alert('Robots at work');")
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()