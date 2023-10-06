import time
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message1()
    page.should_be_message2()








# вопрос к Леониду - почему открывается именно браузер CHROME
# что за метод open без которого ничего не работает и где он иписан
# почуму если я пытаюсь вызвать метод solve_quiz_and_get_code прсое add_product_to_basket то все падает