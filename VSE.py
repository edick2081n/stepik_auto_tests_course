test_main_page.py

from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/it/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message1()
    page.should_be_message2()




base page




product page



locators


