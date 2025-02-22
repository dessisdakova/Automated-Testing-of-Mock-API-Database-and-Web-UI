from test_support.helpers.web_ui.base_page import BasePage
from test_support.helpers.web_ui.locators import *


class LoginPage(BasePage):
    """
    Page object for the login page.
    Inherits from BasePage.
    """

    @property
    def base_url(self) -> str:
        """
        The URL of the login page.

        :return: A string representing the page URL.
        """
        return super().base_url

    @property
    def explicit_wait_locator(self) -> tuple:
        """
        Locator for the element used to verify the page has loaded.

        :return: Locator as tuple.
        """
        return LOGO_DIV

    def login(self, username: str, password: str) -> None:
        """
        Login by entering the username and password, and clicking the login button.

        :param username: The username to log in with.
        :param password: The password to log in with.
        """
        self.driver.find_element(*USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*LOGIN_BUTTON).click()

    def get_error_message(self):
        """Retrieve the message text for unsuccessful login."""
        return self.driver.find_element(*ERROR_HEADER).text
