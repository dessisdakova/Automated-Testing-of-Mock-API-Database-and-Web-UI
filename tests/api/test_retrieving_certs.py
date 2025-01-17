from tests.api.fixtures import *
from test_support.helpers.api.assertions import Assertions


def test_retrieving_root_certificates(root_certs, api_logger):
    """
    Test that a GET request returns the root certificates.
    """
    # act
    get_response = root_certs.get_root_certificates()
    api_logger.debug(f"Sending a GET request to {root_certs.base_url}{root_certs.endpoint}.")

    # assert
    Assertions.assert_status_code(get_response, 200)
    Assertions.assert_response_when_retrieving_certificates(get_response)


def test_retrieving_intermediate_certificates(intermediate_certs, api_logger):
    """
    Test that a GET request returns the intermediate certificates.
    """
    # act
    get_response = intermediate_certs.get_intermediate_certificates()
    api_logger.debug(f"Sending a GET request to {intermediate_certs.base_url}{intermediate_certs.endpoint}.")

    # assert
    Assertions.assert_status_code(get_response, 200)
    Assertions.assert_response_when_retrieving_certificates(get_response)
