from .base_page import BasePage
from .locators import ProducPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        addBtn = self.browser.find_element(*ProducPageLocators.ADD_TO_BASKET)
        addBtn.click()

    def should_be_products_price(self):
        assert self.is_element_present(*ProducPageLocators.PRODUCT_PRICE), "Product's price is missing"

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProducPageLocators.ADD_TO_BASKET), "Add to basket btn is missing"

    def should_be_basket_total_btn(self):
        assert self.is_element_present(*ProducPageLocators.BASKET_TOTAL), "Missing total of products' in basket"

    def should_be_notification_product_added(self):
        assert self.is_element_present(*ProducPageLocators.PRODUCT_ADDED_NOTIF), "Missing notification"

    def should_be_product_title_in_notif(self):
        assert self.is_element_present(*ProducPageLocators.PRODUCT_TITLE_NOTIF), "Missing product's title in notif"

    def should_be_last_added_product_name_in_notif(self):
        productTitleString = self.browser.find_element(*ProducPageLocators.PRODUCT_TITLE)
        productTitle = productTitleString.text
        productTitleNotifString = self.browser.find_element(*ProducPageLocators.PRODUCT_TITLE_NOTIF)
        productTitleInNotif = productTitleNotifString.text
        assert productTitle == productTitleInNotif, f"expect '{productTitle}' in notification, get '{productTitleInNotif}'"

    def should_not_be_success_added_product_notification(self):
        assert self.is_not_element_present(*ProducPageLocators.SUCCESS_MESSAGE), \
            "Notification about successfully added product displays"

    def should_disapper_success_notification(self):
        assert self.is_disappeared(*ProducPageLocators.SUCCESS_MESSAGE), \
            "Notification didn't disappear"
