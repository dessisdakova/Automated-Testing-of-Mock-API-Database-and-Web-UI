from test_support.helpers.web_ui.cart_page import CartPage
from test_support.helpers.web_ui.inventory_page import InventoryPage
from fixtures import *


def test_cart_page_verify_items_in_shopping_cart(driver_logged_in, web_ui_logger):
    """
    Test that added items from Inventory page are present in Cart page.
    """
    # arrange
    web_ui_logger.debug(f"Login with username: standard_user.")
    inventory_page = InventoryPage(driver_logged_in)
    inventory_page.load(5)
    inventory_page.add_item_to_cart("Backpack")
    web_ui_logger.info("'Sauce Labs Backpack' is added to cart.")
    inventory_page.go_to_cart()

    # act
    cart_page = CartPage(driver_logged_in)
    cart_page.load(5)
    web_ui_logger.info(f"Page with url '{cart_page.base_url}' is loaded.")

    # assert
    assert "cart" in inventory_page.get_current_url(), f"Expected text not found in URL."
    assert cart_page.get_items_count_in_cart() == 1, f"Actual items count does not match expected."
    assert "Sauce Labs Backpack" in cart_page.get_item_names_in_cart(), f"Expected item name not found in cart."


def test_cart_page_verify_checkout_button(driver_logged_in, web_ui_logger):
    """
    Test that the Checkout button in Cart page redirects to Checkout step One page.
    """
    # arrange
    web_ui_logger.debug(f"Login with username: standard_user.")
    cart_page = CartPage(driver_logged_in)
    cart_page.load(5)
    web_ui_logger.info(f"Page with url '{cart_page.base_url}' is loaded.")

    # act
    cart_page.click_checkout_button()
    web_ui_logger.info("Checkout button is clicked.")

    # assert
    assert "checkout-step-one" in cart_page.get_current_url(), f"User is not redirected to another page."
