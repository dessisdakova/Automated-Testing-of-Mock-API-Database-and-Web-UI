from test_support.helpers.web_ui.checkout_two_page import CheckoutTwoPage
from test_support.helpers.web_ui.inventory_page import InventoryPage
from fixtures import *


def test_checkout_two_page_verify_items_in_order(driver_logged_in, web_ui_logger):
    """
    Test that items in order in Checkout Two page match the items added in Inventory page.
    """
    # arrange
    web_ui_logger.debug(f"Login with username: standard_user.")
    inventory_page = InventoryPage(driver_logged_in)
    inventory_page.load(5)
    inventory_page.add_item_to_cart("Backpack")
    web_ui_logger.info("'Sauce Labs Backpack' is added to cart.")

    # act
    checkout_two_page = CheckoutTwoPage(driver_logged_in)
    checkout_two_page.load(5)
    web_ui_logger.info(f"Page with url '{checkout_two_page.base_url}' is loaded.")

    # assert
    assert "checkout-step-two" in checkout_two_page.get_current_url(), f"Expected text not found in URL."
    assert checkout_two_page.get_items_count_in_order() == 1, f"Actual items count does not match expected."
    assert "Sauce Labs Backpack" in checkout_two_page.get_item_names_in_cart(), f"Expected item name not found in cart."


def test_checkout_two_page_verify_finish_button(driver_logged_in, web_ui_logger):
    """
    Test that the Finish button redirects to Checkout Complete page.
    """
    # arrange
    web_ui_logger.debug(f"Login with username: standard_user.")
    checkout_two_page = CheckoutTwoPage(driver_logged_in)
    checkout_two_page.load(5)
    web_ui_logger.info(f"Page with url '{checkout_two_page.base_url}' is loaded.")

    # act
    checkout_two_page.click_finish_button()
    web_ui_logger.info("Finish button is clicked.")

    # assert
    assert "checkout-complete" in checkout_two_page.get_current_url(), f"User is not redirected to another page."
