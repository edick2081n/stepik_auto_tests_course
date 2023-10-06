#import sys
#sys.path.append("C:\\Users\\Eduard\\sites\\Selenium")
import math


from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import email, password
from selenium.webdriver.common.keys import Keys
#from Selenium.config import email
#from ..config import email, password
import pytest


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1"

                                ])
def test_login(browser, link):
  #  link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    #time.sleep(10)
    button_enter = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-view.navbar__auth"))
    )
        #browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth")



    button_enter.click()
    login_email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    login_password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    button_green = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn"))
    )
   #     browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")

    login_email.send_keys(email)
    login_password.send_keys(password)
    button_green.click()
    answer = math.log(int(time.time()+6.5))

    field_for_send = browser.find_element(By.XPATH, "//textarea")
   #time.sleep(1)
   # field_for_send.send_keys(Keys.BACK_SPACE)
    #time.sleep(5)
    field_for_send.clear()
    #time.sleep(5)
    field_for_send.send_keys(answer)
    button_send = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )




    button_send.click()
    check_element = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    check_element_text = check_element.text
    a=""
    if check_element_text != "Correct!":
        a+=check_element_text
    print(a)
 #   assert check_element_text=="Correct!", f"{check_element_text} received data is not corrected"


    # ожидание чтобы визуально оценить результаты прохождения скрипта



    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()



# @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
#                                 "https://stepik.org/lesson/236896/step/1",
#                                 "https://stepik.org/lesson/236897/step/1",
#                                 "https://stepik.org/lesson/236898/step/1",
#                                 "https://stepik.org/lesson/236899/step/1",
#                                 "https://stepik.org/lesson/236903/step/1",
#                                 "https://stepik.org/lesson/236904/step/1",
#                                 "https://stepik.org/lesson/236905/step/1"
#                                 ])


# def test_guest_should_see_login_link(browser, link):
#
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")
#
