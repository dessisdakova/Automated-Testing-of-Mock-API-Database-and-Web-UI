from test_support.common.create_logger import create_logger
import pytest
from pytest_custom_outputs import get_results


@pytest.fixture(scope="session")
def api_logger():
    return create_logger("api_logger", "api_tests")


@pytest.fixture(scope="session")
def db_logger():
    return create_logger("db_logger", "db_tests")


@pytest.fixture(scope="session")
def web_ui_logger():
    return create_logger("web_ui_logger", "web_ui_tests")


@pytest.fixture(scope="function", autouse=True)
def log_test_start_and_result(request) -> None:
    """
    Fixture to log the start and result of each test.

    :param request: The pytest request object providing information about the current test.
    """
    if "api" in request.node.nodeid:
        logger = request.getfixturevalue("api_logger")
    elif "db" in request.node.nodeid:
        logger = request.getfixturevalue("db_logger")
    elif "web_ui" in request.node.nodeid:
        logger = request.getfixturevalue("web_ui_logger")
    else:
        raise ValueError(f"Cannot determine the logger for test: {request.node.nodeid}")

    logger.info(f" === {request.node.name} === ")
    yield
    if get_results(request)["status"] == "passed":
        logger.info("Test PASSED.\n")
    elif get_results(request)["status"] == "failed":
        logger.error(f"Test FAILED. \n Error: \n {get_results(request)['message']}\n")
    else:
        logger.warning(f"Test {get_results(request)['status']}.\n")
