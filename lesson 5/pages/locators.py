from selenium.webdriver.common.by import By
from stere.strategy import FindById


class MainPageLocators:
    LOGIN_LINK = (FindById.strategy, "login_link")

class LoginPageLocators:
    LOGIN_USER_NAME = (By.CSS_SELECTOR, "#id_login-username")
    lOGIN_USER_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_NAME = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators:
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div h1")
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, "div .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_page .price_color")
    CURRENT_AMOUNT_BASKET = (By.CSS_SELECTOR, "#messages p strong")




# ВОПРОС К ЛЕОНИДУ - ФОРМА ЗАПИСАИ БЕЗ FIND ELEMENTS
