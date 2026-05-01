from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def title(self) -> str:
        return self.text_of(self.TITLE)

    def item_names(self) -> list[str]:
        return [item.text for item in self.elements(self.ITEM_NAMES)]

    def item_count(self) -> int:
        return len(self.elements(self.CART_ITEMS))

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait_until_url_contains("checkout-step-one.html")
