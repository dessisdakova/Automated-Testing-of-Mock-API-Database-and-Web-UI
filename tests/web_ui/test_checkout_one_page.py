from test_support.common.yaml_loaders import load_web_ui_test_data
from test_support.helpers.web_ui.checkout_one_page import CheckoutOnePage
from tests.web_ui.fixtures import *


@pytest.mark.parametrize("input_data", load_web_ui_test_data("checkout_one_page_buyer_information"))
def test_checkout_one_page_verify_continue_button_with_buyer_information(driver_logged_in, input_data, web_ui_logger):
    """
    Test that the Continue button in Checkout One page
    redirects to Checkout Two page when buyer information is filled.
    """
    # arrange
    web_ui_logger.debug(f"Login with username: standard_user.")
    checkout_one_page = CheckoutOnePage(driver_logged_in)
    checkout_one_page.load(5)
    web_ui_logger.info(f"Page with url '{checkout_one_page.base_url}' is loaded.")

    # act
    checkout_one_page.enter_buyer_info(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])
    web_ui_logger.info("Buyer's information is filled.")
    checkout_one_page.click_continue_button()
    web_ui_logger.info("Continue button is clicked.")

    # assert
    assert "checkout-step-two" in checkout_one_page.get_current_url(), f"Expected text not found in URL."


def test_checkout_one_page_verify_continue_button_without_buyer_information(driver_logged_in, web_ui_logger):
    """
    Test that the Continue button in Checkout One page
    does not redirect to Checkout Two page when buyer information is not filled.
    """
    # arrange
    web_ui_logger.debug(f"Login with username: standard_user.")
    checkout_one_page = CheckoutOnePage(driver_logged_in)
    checkout_one_page.load(5)
    web_ui_logger.info(f"Page with url '{checkout_one_page.base_url}' is loaded.")

    # act
    checkout_one_page.click_continue_button()
    web_ui_logger.info("Continue button is clicked.")

    # assert
    assert "checkout-step-one" in checkout_one_page.get_current_url(), f"User is redirected to another page."
