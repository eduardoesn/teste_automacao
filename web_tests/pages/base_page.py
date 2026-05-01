from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def click_until_visible(self, click_locator, visible_locator):
        for _ in range(3):
            self.click(click_locator)
            if self.is_visible(visible_locator):
                return
        self.wait_until_visible(visible_locator)

    def javascript_click(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text: str):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def text_of(self, locator) -> str:
        return self.wait.until(ec.visibility_of_element_located(locator)).text

    def elements(self, locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def wait_until_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def wait_until_text_is(self, locator, expected_text: str):
        return self.wait.until(ec.text_to_be_present_in_element(locator, expected_text))

    def wait_until_url_contains(self, text: str):
        return self.wait.until(ec.url_contains(text))

    def is_visible(self, locator) -> bool:
        try:
            self.wait_until_visible(locator)
            return True
        except (StaleElementReferenceException, TimeoutException):
            return False
