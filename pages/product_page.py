# noinspection PyUnresolvedReferences
from .base_page import BasePage
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def should_be_opened_product_page_url(self):
        assert "?promo=newYear" in self.browser.current_url, "product_page url is not presented"
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
    def should_be_success_message(self):
        success_text_elt = self.browser.find_element(*ProductPageLocators.success_text)
        success_text = success_text_elt.text
        assert "The shellcoder's handbook" == success_text, "product isn't added to basket "
    def should_be_right_product_price(self):
        basket_price_elt = self.browser.find_element(*ProductPageLocators.basket_price)
        basket_price = basket_price_elt.text
        product_price_elt = self.browser.find_element(*ProductPageLocators.product_price)
        product_price = product_price_elt.text
        assert basket_price == product_price, "The cost of the basket isn't equal to the price of the good"

