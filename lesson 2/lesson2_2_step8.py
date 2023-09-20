#  Задание: загрузка файла
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Вова")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Вовин")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("123@list.ru")
    choice1 = browser.find_element(By.ID, "file")
    choice1.send_keys('C:\\Users\\Eduard\\sites\\Selenium\\grizly.jpg')
    button = browser.find_element(By.CSS_SELECTOR, "button,btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

