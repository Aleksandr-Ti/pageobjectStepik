from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_see_login_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    lpage = LoginPage(browser, browser.current_url)
    lpage.should_be_login_form()

def test_guest_can_see_registr_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    lpage = LoginPage(browser, browser.current_url)
    lpage.should_be_register_form()


def test_guest_on_correct_url(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    lpage = LoginPage(browser, browser.current_url)
    lpage.should_be_login_url()