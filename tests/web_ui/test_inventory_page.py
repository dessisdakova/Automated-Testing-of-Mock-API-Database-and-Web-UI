from test_support.common.yaml_loaders import load_web_ui_test_data
from test_support.helpers.web_ui.inventory_page import InventoryPage
from tests.web_ui.fixtures import *


@pytest.mark.parametrize("input_data", load_web_ui_test_data("inventory_page_items"))
def test_add_item_to_cart(driver_logged_in, input_data, web_ui_logger):
    """
    Test that items can be added from Inventory page into shopping cart.
    """
    # arrange
    inventory_page = InventoryPage(driver_logged_in)
    inventory_page.load(5)
    web_ui_logger.debug(f"Page with url '{inventory_page.base_url}' is loaded.")

    # act
    inventory_page.add_item_to_cart(input_data["item"])
    web_ui_logger.debug(f"Adding Sauce Labs {input_data['item']} to cart.")

    # assert
    assert inventory_page.get_items_count_in_cart() == 1, f"Item was not added to cart."
