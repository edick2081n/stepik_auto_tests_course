from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")



# price_element = browser.find_element(By.ID, "price")
# price = price_element.text

button = browser.find_element(By.ID, "book")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button.click()
#browser.implicitly_wait(5)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
#time.sleep(3)
input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)
button = browser.find_element(By.ID, "solve")
button.click()
time.sleep(8)









