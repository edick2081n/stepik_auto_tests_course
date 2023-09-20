#  Задание на execute_script
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__=="__main__":

    try:
        link = "https://SunInJuly.github.io/execute_script.html"
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
        input1.send_keys(y)
        # js для прокрутки страницы вниз (scroll)
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
        input2.click()
        input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
        input3.click()

        button.click()


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

