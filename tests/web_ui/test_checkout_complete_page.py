from test_support.helpers.web_ui.checkout_complete_page import CheckoutCompletePage
from fixtures import *


def test_checkout_complete_page_verify_message(driver_logged_in, web_ui_logger):
    """
    Test that the message for complete order in present.
    """
    # arrange
    web_ui_logger.debug(f"Login with username: standard_user.")

    # act
    checkout_complete = CheckoutCompletePage(driver_logged_in)
    checkout_complete.load(5)
    web_ui_logger.info(f"Page with url '{checkout_complete.base_url}' is loaded.")

    # assert
    assert "checkout-complete" in checkout_complete.get_current_url(), f"Expected text not found in URL."
    assert "Thank you for your order!" in checkout_complete.get_message_text(), f"Order was not completed."
