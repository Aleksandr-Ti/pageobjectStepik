from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_add_product_to_basket(browser):
    productpage = ProductPage(browser, link)
    productpage.open()
    productpage.add_product_to_basket()
    quiz = BasePage (browser, link)
    quiz.solve_quiz_and_get_code()

def test_product_title_in_notif(browser):
    productpage = ProductPage(browser, link)
    productpage.open()
    productpage.add_product_to_basket()
    quiz = BasePage(browser, link)
    quiz.solve_quiz_and_get_code()
    productpage.should_be_last_added_product_name_in_notif()