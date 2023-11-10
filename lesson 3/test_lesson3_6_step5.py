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


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"
                                 ])
def test_login(browser, link):
    browser.get(link)
    # поиск кнопки "войти" для регистрации
    button_enter = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-view.navbar__auth"))
    )

    button_enter.click()
    # поиск полей необходимых к заполнению для регистрации
    login_email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    login_password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    # поиск кнопки для завершения регистрации
    button_green = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn"))
    )
    # заполнение полей и нажатие на кнопку завершения регистрации
    login_email.send_keys(email)
    login_password.send_keys(password)
    button_green.click()
    # вычисление значения математической функции
    time.sleep(10)
    answer = math.log(int(time.time()+6.5))

    # поиск кнопки " решить снова"
    try:
        button_again = browser.find_element(By.XPATH, "//button[text()='Решить снова']")
        button_again.click()
        time.sleep(5)
    except:
        time.sleep(5)

    finally:
        time.sleep(10)
        # поиск поля для ввода рассчитанного значения математ. функции

        field_for_send = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//textarea")))
        #browser.find_element(By.XPATH, "//textarea")
        field_for_send.clear()

        field_for_send.send_keys(answer)
        # поиск поля для отправки рассчитанного значения математ. функции
        button_send = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        time.sleep(10)
        button_send.click()
        time.sleep(10)
        check_element = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
        check_element_text = check_element.text
        incorrect_string=""
        if check_element_text != "Correct!":
            incorrect_string+=check_element_text

        print("IMCORRECT STRING",incorrect_string)
     #   assert check_element_text=="Correct!", f"{check_element_text} received data is not corrected"
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()


