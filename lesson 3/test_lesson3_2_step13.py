import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


class TestSelector(unittest.TestCase):
    def do_registration(self, link):

        browser = webdriver.Chrome()

        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CLASS_NAME, "first")
        input1.send_keys("Вова")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Вовин")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.third")
        input3.send_keys("vova@list.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)



        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Congratulations! You have successfully registered!" == welcome_text


        # # ожидание чтобы визуально оценить результаты прохождения скрипта
        # time.sleep(10)
        # # закрываем браузер после всех манипуляций
        # browser.quit()


        return welcome_text


    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        message = self.do_registration(link)
        self.assertEqual("Congratulations! You have successfully registered!", message, "Wrong selector")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        message = self.do_registration(link)
        self.assertEqual("Congratulations! You have successfully registered!", message, "Wrong selector")


if __name__ == "__main__":
    unittest.main()

# Вопрос к Леониду как вызвать функцию тестирования из этого файла елси класс обьявить в конце а не в начале
# как использовать в тестах конструкцию try finally