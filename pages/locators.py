from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner strong")
    REAL_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")

    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
