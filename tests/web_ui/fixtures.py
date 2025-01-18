from test_support.common.yaml_loaders import load_config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest
from typing import Generator

from test_support.helpers.web_ui.login_page import LoginPage


@pytest.fixture(scope="function")
def driver(web_ui_logger) -> Generator[webdriver.Remote, None, None]:
    """
    Fixture to initialize a web driver for tests based on the configuration.

    This fixture sets up the selected browser (Chrome, Firefox, or Edge) in headless mode
    and creates a remote WebDriver instance. It also sets an implicit wait time.

    :param web_ui_logger: Logger instance.
    :return: A web driver instance to be used for the duration of each test.
    """

    config = load_config("web_ui_config")
    if config["browser"] == "chrome":
        options = ChromeOptions()
    elif config["browser"] == "firefox":
        options = FirefoxOptions()
    elif config["browser"] == "edge":
        options = EdgeOptions()
    else:
        raise ValueError(f"Unsupported browser: '{config['browser']}'")
    options.add_argument("--headless")

    driver = webdriver.Remote(command_executor=config["executor"], options=options)
    web_ui_logger.info(f"Initialized WebDriver for {driver.capabilities['browserName']} "
                       f"version {driver.capabilities['browserVersion']}.")
    driver.implicitly_wait(config["implicit_wait_time"])
    web_ui_logger.info(f"Implicit wait time: {config['implicit_wait_time']} seconds.")

    yield driver

    driver.quit()
    web_ui_logger.info(f"WebDriver is closed.")


@pytest.fixture(scope="function")
def login_page(driver):
    """Fixture to create Login page instance and load it."""
    login_page = LoginPage(driver)
    login_page.load(5)
    return login_page
