from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    EMAIL_INPUT_REGISTER = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_REGISTER = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_INPUT_REGISTER_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert")

    ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner strong")
    REAL_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")

    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    GOODS = (By.CSS_SELECTOR, "#basket_formset")
