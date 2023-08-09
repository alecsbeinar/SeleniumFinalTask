from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_message_basket_is_empty()
        self.should_not_be_goods()

    def should_not_be_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS), "Basket is not empty\n"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Message that basket is empty is not presented\n"
