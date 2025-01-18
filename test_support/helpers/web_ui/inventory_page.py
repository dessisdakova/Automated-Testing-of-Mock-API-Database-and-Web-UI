from test_support.helpers.web_ui.base_page import BasePage
from test_support.helpers.web_ui.locators import *


class InventoryPage(BasePage):
    """
    Page object for the inventory page.
    Inherits from BasePage.
    """
    @property
    def base_url(self) -> str:
        """
        The URL of the inventory page.

        :return: A string representing the inventory page URL.
        """
        return super().base_url + "inventory.html"

    @property
    def explicit_wait_locator(self) -> tuple:
        """
        Locator for the element used to verify the inventory page has loaded.

        :return: Locator tuple for the inventory container.
        """
        return INVENTORY_CONTAINER

    def add_item_to_cart(self, item: str) -> None:
        """
        Add item to cart based on the following values:
         - "Backpack" - adds Sauce Labs Backpack
         - "Bike Light" - adds Sauce Labs Bike Light
         - "Bolt T-Shirt" - adds Sauce Labs Bolt T-Shirt
         - "Fleece Jacket" - adds Sauce Labs Fleece Jacket
         - "Onesie" - adds Sauce Labs Onesie

        :param item: Must be one of the provided values.
        """
        if item == "Backpack":
            self.driver.find_element(*ADD_BACKPACK_BUTTON).click()
        elif item == "Bike Light":
            self.driver.find_element(*ADD_BIKE_LIGHT_BUTTON).click()
        elif item == "Bolt T-Shirt":
            self.driver.find_element(*ADD_BOLT_T_SHIRT_BUTTON).click()
        elif item == "Fleece Jacket":
            self.driver.find_element(*ADD_FLEECE_JACKET_BUTTON).click()
        elif item == "Onesie":
            self.driver.find_element(*ADD_ONESIE_BUTTON).click()
        else:
            raise ValueError(f"Unknown item '{item}'!")

    def get_items_count_in_cart(self) -> int:
        """
        Retrieve items count in cart from shopping cart badge.
        """
        items = self.driver.find_element(*SHOPPING_CART_BADGE).text
        return int(items)

    def go_to_cart(self) -> None:
        """
        Navigate to the shopping cart page by clicking the cart link.
        """
        self.driver.find_element(*SHOPPING_CART_LINK).click()

