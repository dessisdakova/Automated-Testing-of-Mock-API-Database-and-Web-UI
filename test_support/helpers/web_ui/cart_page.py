from test_support.helpers.web_ui.base_page import BasePage
from test_support.helpers.web_ui.locators import *


class CartPage(BasePage):
    """
    Page object for the cart page.
    Inherits from BasePage.
    """
    @property
    def base_url(self) -> str:
        """
        The URL of the cart page.

        :return: A string representing the page URL.
        """
        return super().base_url + "cart.html"

    @property
    def explicit_wait_locator(self) -> tuple:
        """
        Locator for the element used to verify the cart page has loaded.

        :return: Locator as tuple.
        """
        return CART_CONTENTS_CONTAINER

    def get_items_count_in_cart(self) -> int:
        """
        Retrieve all items in the cart.

        :return: The number of items added to the cart.
        """
        return len(self.driver.find_elements(*ITEMS_IN_CART))

    def get_item_names_in_cart(self) -> list:
        """
        Retrieve the names of all items in the cart.

        :return: A list of item names added to the cart.
        """
        elements = self.driver.find_elements(*ITEMS_NAME_IN_CART)
        return [element.text for element in elements]

    def click_checkout_button(self) -> None:
        """
        Navigate to the checkout step one page by clicking the checkout button.
        """
        self.driver.find_element(*CHECKOUT_BUTTON).click()
