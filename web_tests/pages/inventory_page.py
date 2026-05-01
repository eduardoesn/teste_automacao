from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BACKPACK_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    BIKE_LIGHT_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-bike-light")

    def title(self) -> str:
        return self.text_of(self.TITLE)

    def add_backpack(self):
        self._add_product(self.BACKPACK_ADD_BUTTON, self.BACKPACK_REMOVE_BUTTON)

    def add_bike_light(self):
        self._add_product(self.BIKE_LIGHT_ADD_BUTTON, self.BIKE_LIGHT_REMOVE_BUTTON)

    def cart_quantity(self) -> str:
        return self.text_of(self.CART_BADGE)

    def wait_for_cart_quantity(self, quantity: str):
        self.wait_until_text_is(self.CART_BADGE, quantity)

    def open_cart(self):
        self.click(self.CART_LINK)
        self.wait_until_url_contains("cart.html")

    def _add_product(self, add_locator, remove_locator):
        self.click_until_visible(add_locator, remove_locator)
