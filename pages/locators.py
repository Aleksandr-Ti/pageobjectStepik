from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProducPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    PRODUCT_ADDED_NOTIF = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_TITLE_NOTIF = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
