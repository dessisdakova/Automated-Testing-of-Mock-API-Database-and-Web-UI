from test_support.helpers.web_ui.base_page import BasePage
from test_support.helpers.web_ui.locators import *


class CheckoutCompletePage(BasePage):
    """
    Page object for the checkout complete page.
    Inherits from BasePage.
    """

    @property
    def base_url(self):
        """
        The URL of the checkout complete page.

        :return: A string representing the page URL.
        """
        return super().base_url + "checkout-complete.html"

    @property
    def explicit_wait_locator(self) -> tuple:
        """
        Locator for the element used to verify the checkout complete page has loaded.

        :return: Locator as tuple.
        """
        return CHECKOUT_COMPLETE_CONTAINER

    def get_message_text(self) -> str:
        """
        Retrieve the text from the message header element.

        :return: The text content of the message header.
        """
        return self.driver.find_element(*MESSAGE_HEADER).text
