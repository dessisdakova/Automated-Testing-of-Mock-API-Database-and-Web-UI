from test_support.common.yaml_loaders import load_web_ui_test_data
from tests.web_ui.fixtures import *


@pytest.mark.parametrize("input_data", load_web_ui_test_data("login_page_valid_users"))
def test_login_with_valid_users(driver, input_data, web_ui_logger):
    """
    Login with valid users should redirect to Inventory page.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    web_ui_logger.info(f"Page with url '{login_page.base_url}' is loaded.")

    # act
    login_page.login(input_data["username"], input_data["password"])
    web_ui_logger.debug(f"Login with username: {input_data['username']}.")
    web_ui_logger.debug(f"Login with password: {input_data['password']}.")

    # assert
    assert "inventory" in login_page.get_current_url(), f"Unsuccessful login."


@pytest.mark.parametrize("input_data", load_web_ui_test_data("login_page_invalid_users"))
def test_login_with_invalid_users(driver, input_data, web_ui_logger):
    """
    Login with invalid users should keep user on Login page and show error message..
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    web_ui_logger.info(f"Page with url '{login_page.base_url}' is loaded.")

    # act
    login_page.login(input_data["username"], input_data["password"])
    web_ui_logger.debug(f"Login with username: {input_data['username']}.")
    web_ui_logger.debug(f"Login with password: {input_data['password']}.")

    # assert
    assert "https://www.saucedemo.com/" == login_page.get_current_url(), f"User is redirected to another page."
    assert "Username and password do not match any user in this service" in login_page.get_error_message(), \
        "Error message is not present or does not match."


@pytest.mark.parametrize("input_data", load_web_ui_test_data("login_page_locked_out_user"))
def test_login_with_locked_out_user(driver, input_data, web_ui_logger):
    """
    Login with locked out user should keep user on Login page and show error message.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    web_ui_logger.info(f"Page with url '{login_page.base_url}' is loaded.")

    # act
    login_page.login(input_data["username"], input_data["password"])
    web_ui_logger.debug(f"Login with username: {input_data['username']}.")
    web_ui_logger.debug(f"Login with password: {input_data['password']}.")

    # assert
    assert "https://www.saucedemo.com/" == login_page.get_current_url(), f"User is redirected to another page."
    assert "Sorry, this user has been locked out." in login_page.get_error_message(), \
        "Error message is not present or does not match."
