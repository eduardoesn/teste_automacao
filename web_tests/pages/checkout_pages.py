from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage


class CheckoutInformationPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def title(self) -> str:
        return self.text_of(self.TITLE)

    def fill_customer_data(self, first_name: str, last_name: str, postal_code: str):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)
        self.wait_until_url_contains("checkout-step-two.html")


class CheckoutOverviewPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")

    def title(self) -> str:
        return self.text_of(self.TITLE)

    def total(self) -> str:
        return self.text_of(self.SUMMARY_TOTAL)

    def finish(self):
        self.click(self.FINISH_BUTTON)
        self.wait_until_url_contains("checkout-complete.html")


class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def success_message(self) -> str:
        return self.text_of(self.COMPLETE_HEADER)
