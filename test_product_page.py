from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_opened_product_page_url()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message()
    product_page.should_be_right_product_price()
