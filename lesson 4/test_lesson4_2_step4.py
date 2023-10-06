from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


  # Вопрос к Леониду - почему не проходит тест с указанием языка pytest -v --tb=line --language=en "lesson 4test_lesson4_2_step4.py"
  # Опять ошибки связанные с сертификатом - как их убрать
  # НЕ ПОНИМАЮ А ГДЕ ОБРАЩЕНИЕ К CHROME - НАВЕРНОЕ ФАЙЛ CONFEST.PY
  # ОТКУДА ИЗВЕСТНО ЧТО У ОБЬЕКТА PAGE ЕСТЬ ЕСТЬ МЕТОД OPEN