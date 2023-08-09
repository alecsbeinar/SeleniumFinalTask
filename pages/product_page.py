from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to busket button is not presented\n"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be\n"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared\n"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_success_message(self):
        added_product = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT).text
        real_product = self.browser.find_element(*ProductPageLocators.REAL_PRODUCT).text
        assert added_product == real_product, "Added wrong product to basket\n"
        basket_total_cash = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_total_cash == product_price, "Difference in real and added price\n"
