from .pages.product_page import ProductPage
from .pages.base_page import BasePage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_add_product_to_basket(browser, link):
    productpage = ProductPage(browser, link)
    productpage.open()
    productpage.add_product_to_basket()
    quiz = BasePage (browser, link)
    quiz.solve_quiz_and_get_code()


def test_product_title_in_notif(browser, link):
    productpage = ProductPage(browser, link)
    productpage.open()
    productpage.add_product_to_basket()
    quiz = BasePage(browser, link)
    quiz.solve_quiz_and_get_code()
    productpage.should_be_last_added_product_name_in_notif()