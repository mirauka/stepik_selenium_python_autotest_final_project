from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_success_message(self):
        self.should_be_correct_book()
        self.should_be_correct_price()

    def return_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return book_name

    def return_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        return book_price

    def should_be_correct_book(self):
        success_message_book_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BOOK_NAME).text
        assert self.return_book_name() == success_message_book_name, f"Incorrect book name in success message. Should be: '{self.return_book_name()}', you got: '{success_message_book_name}'"

    def should_be_correct_price(self):
        success_message_book_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BOOK_PRICE).text
        assert self.return_book_price() == success_message_book_price, f"Incorrect book price in success message. Should be: '{self.return_book_price()}', you got: '{success_message_book_price}'"