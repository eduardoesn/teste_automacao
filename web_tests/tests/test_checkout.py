import os
import shutil
import tempfile
from pathlib import Path

import pytest
from selenium.common.exceptions import NoSuchDriverException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from web_tests.pages.cart_page import CartPage
from web_tests.pages.checkout_pages import (
    CheckoutCompletePage,
    CheckoutInformationPage,
    CheckoutOverviewPage,
)
from web_tests.pages.inventory_page import InventoryPage
from web_tests.pages.login_page import LoginPage


@pytest.fixture
def driver():
    os.environ.setdefault("SE_MANAGER_CACHE_PATH", str(Path(".selenium_cache").resolve()))
    profile_dir = tempfile.mkdtemp(prefix="saucedemo-profile-")

    options = Options()
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,768")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--password-store=basic")
    options.add_argument(f"--user-data-dir={profile_dir}")
    options.add_argument(
        "--disable-features=PasswordLeakDetection,PasswordManagerOnboarding,"
        "AutofillServerCommunication"
    )
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
        },
    )

    driver_path = os.getenv("CHROME_DRIVER_PATH")
    service = Service(executable_path=driver_path) if driver_path else Service()

    try:
        browser = webdriver.Chrome(service=service, options=options)
    except NoSuchDriverException as error:
        pytest.fail(
            "Nao foi possivel iniciar o ChromeDriver. "
            "Instale o Google Chrome e rode o teste com internet no primeiro uso, "
            "ou informe o caminho do driver com CHROME_DRIVER_PATH.",
            pytrace=False,
        )

    browser.implicitly_wait(5)
    try:
        yield browser
    finally:
        browser.quit()
        shutil.rmtree(profile_dir, ignore_errors=True)


def test_complete_checkout_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_information_page = CheckoutInformationPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(ec.url_contains("inventory"))
    assert inventory_page.title() == "Products"

    inventory_page.add_backpack()
    inventory_page.wait_for_cart_quantity("1")
    inventory_page.add_bike_light()
    inventory_page.wait_for_cart_quantity("2")
    assert inventory_page.cart_quantity() == "2"

    inventory_page.open_cart()
    assert cart_page.title() == "Your Cart"
    assert cart_page.item_count() == 2
    assert cart_page.item_names() == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    cart_page.checkout()
    assert checkout_information_page.title() == "Checkout: Your Information"
    checkout_information_page.fill_customer_data("Eduardo", "Automacao", "01001000")
    assert checkout_overview_page.title() == "Checkout: Overview"
    assert checkout_overview_page.total().startswith("Total: $")

    checkout_overview_page.finish()
    assert checkout_complete_page.success_message() == "Thank you for your order!"

    screenshots_dir = Path("artifacts/screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(str(screenshots_dir / "checkout-completo.png"))
