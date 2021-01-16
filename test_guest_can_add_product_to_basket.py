from .pages.product_page import ProductPage
from .pages.base_page import BasePage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_product_to_basket(browser):
    productpage = ProductPage(browser, link)
    productpage.open()
    productpage.add_product_to_basket()
    #quiz = BasePage (browser, link)
    #quiz.solve_quiz_and_get_code()

def test_product_title_in_notif(browser):
    productpage = ProductPage(browser, link)
    productpage.open()
    productpage.add_product_to_basket()
    #quiz = BasePage(browser, link)
    #quiz.solve_quiz_and_get_code()
    productpage.should_be_last_added_product_name_in_notif()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    productpage = ProductPage(browser, link)
    productpage.open()
    productpage.add_product_to_basket()
    productpage.should_not_be_success_added_product_notification()

def test_guest_cant_see_success_message(browser):
    productpage = ProductPage(browser, link)
    productpage.open()
    productpage.should_not_be_success_added_product_notification()

def test_message_disappeared_after_adding_product_to_basket(browser):
    productpage = ProductPage(browser, link)
    productpage.open()
    productpage.add_product_to_basket()
    productpage.should_disapper_success_notification()

