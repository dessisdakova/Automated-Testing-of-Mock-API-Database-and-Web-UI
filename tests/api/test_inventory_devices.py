from tests.api.fixtures import *
from test_support.common.yaml_loaders import load_api_test_data
from test_support.helpers.api.assertions import Assertions
import requests
import json


def test_get_request_retrieving_currently_saved_devices(inventory_devices, api_logger):
    """
    Test that a GET request retrieves the currently saved inventory devices successfully.
    """
    # arrange
    expected_keys = ["build", "deviceAddresses", "id", "ipAddress", "model", "serialNum", "version"]
    sub_key = "deviceAddresses"
    expected_device_addresses_keys = ["fqdn", "ipv4Address", "ipv6Address"]

    # act
    get_response = inventory_devices.get_devices()
    api_logger.debug(f"Sending a GET request to {inventory_devices.base_url}{inventory_devices.endpoint}.")

    # assert
    Assertions.assert_status_code(get_response, 200)
    Assertions.assert_response_is_json(get_response)
    Assertions.assert_keys_in_inventory_device(get_response, expected_keys)
    Assertions.assert_sub_keys_for_key_in_inventory_device(get_response, sub_key, expected_device_addresses_keys)


@pytest.mark.parametrize("test_data", load_api_test_data("api_inventory")["Different_types_and_missing_values_in_body_key"])
def test_put_request_change_response_of_get_request(inventory_devices, test_data, api_logger):
    """
    Test that a PUT request with missing and different types of keys in devices
    updates successfully the response of subsequent GET requests.
    """
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }
    api_logger.debug(f"Request body:\n{json.dumps(body, indent=4)}")
    expected_keys = ["new_body", "new_status_code"]

    # act
    put_response = inventory_devices.update_devices_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {inventory_devices.base_url}{inventory_devices.endpoint}.")
    get_response = inventory_devices.get_devices()
    api_logger.debug(f"Sending a GET request to {inventory_devices.base_url}{inventory_devices.endpoint}.")

    # assert PUT request
    # Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # assert GET request
    Assertions.assert_get_response_matches_put_request(get_response, put_response)


@pytest.mark.parametrize("test_data", load_api_test_data("api_inventory")["Status_code_valid_number"])
def test_put_request_when_status_code_is_an_integer_with_valid_code(inventory_devices, test_data, api_logger):
    """
    Test that a PUT request with a valid integer status_code
    updates successfully the response of subsequent GET requests.
    """
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }
    api_logger.debug(f"Request body:\n{json.dumps(body, indent=4)}")

    expected_keys = ["new_body", "new_status_code"]

    # act
    put_response = inventory_devices.update_devices_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {inventory_devices.base_url}{inventory_devices.endpoint}.")
    get_response = inventory_devices.get_devices()
    api_logger.debug(f"Sending a GET request to {inventory_devices.base_url}{inventory_devices.endpoint}.")

    # assert PUT request
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # assert GET request
    Assertions.assert_get_response_matches_put_request(get_response, put_response)


@pytest.mark.parametrize("test_data", load_api_test_data("api_inventory")["Status_code_object"])
def test_put_request_when_status_code_is_sent_an_object(inventory_devices, test_data, api_logger):
    """
    Test that a PUT request with a status_code as an object
    updates successfully the response of subsequent GET requests.
    """
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }
    api_logger.debug(f"Request body:\n{json.dumps(body, indent=4)}")

    expected_keys = ["new_body", "new_status_code"]

    # act
    put_response = inventory_devices.update_devices_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {inventory_devices.base_url}{inventory_devices.endpoint}.")
    get_response = inventory_devices.get_devices()
    api_logger.debug(f"Sending a GET request to {inventory_devices.base_url}{inventory_devices.endpoint}.")

    # assert PUT request
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # assert GET request
    Assertions.assert_get_response_matches_put_request(get_response, put_response)


@pytest.mark.parametrize("test_data", load_api_test_data("api_inventory")["Missing_body_or_status_code_key"])
def test_put_request_when_key_in_body_is_missing(inventory_devices, test_data, api_logger):
    """
    Test that a PUT request missing required key returns 500 Internal Server Error.
    """
    # arrange
    body = test_data
    api_logger.debug(f"Request body:\n{json.dumps(body, indent=4)}")

    # act
    put_response = inventory_devices.update_devices_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {inventory_devices.base_url}{inventory_devices.endpoint}.")

    # assert
    Assertions.assert_internal_server_error_response(put_response)


def test_put_request_when_body_is_missing(inventory_devices, api_logger):
    """
    Test that a PUT request with missing body returns 400 Bad Request.
    """
    # act
    put_response = inventory_devices.update_devices_and_status_code(body=None)
    api_logger.debug(f"Sending a PUT request to {inventory_devices.base_url}{inventory_devices.endpoint}.")

    # assert
    Assertions.assert_status_code(put_response, 400)


@pytest.mark.parametrize("test_data", load_api_test_data("api_inventory")["Status_code_array_float"])
def test_put_request_when_status_code_is_sent_as_an_array_or_float(inventory_devices, test_data, api_logger):
    """
    Test that a PUT request with a status_code sent as an array or float
    changes response of GET request to 500 Internal Server Error.
    """
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }
    api_logger.debug(f"Request body:\n{json.dumps(body, indent=4)}")

    expected_keys = ["new_body", "new_status_code"]

    # act
    put_response = inventory_devices.update_devices_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {inventory_devices.base_url}{inventory_devices.endpoint}.")
    get_response = inventory_devices.get_devices()
    api_logger.debug(f"Sending a GET request to {inventory_devices.base_url}{inventory_devices.endpoint}.")

    # assert PUT request
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # assert GET request
    Assertions.assert_internal_server_error_response(get_response)


@pytest.mark.parametrize("test_data", load_api_test_data("api_inventory")["Status_code_invalid_string"])
def test_put_request_when_status_code_is_sent_as_invalid_string(inventory_devices, test_data, api_logger):
    """
    Test that a PUT request with an invalid string as the status_code prevents further execution of a GET request.
    """
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }
    api_logger.debug(f"Request body:\n{json.dumps(body, indent=4)}")

    expected_keys = ["new_body", "new_status_code"]

    # act
    put_response = inventory_devices.update_devices_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {inventory_devices.base_url}{inventory_devices.endpoint}.")

    # assert PUT request
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # a GET request can not be sent
    with pytest.raises(requests.exceptions.RequestException):
        inventory_devices.get_devices()


@pytest.mark.parametrize("test_data", load_api_test_data("api_inventory")["Status_code_invalid_number"])
def test_put_request_when_status_code_is_an_integer_with_invalid_code(inventory_devices, test_data, api_logger):
    """
    Test that a PUT request with an invalid integer as the status_code prevents further execution of a GET request.
    """
    # arrange
    body = {
        "body": test_data["body"],
        "status_code": test_data["status_code"]
    }
    api_logger.debug(f"Request body:\n{json.dumps(body, indent=4)}")

    expected_keys = ["new_body", "new_status_code"]

    # act
    put_response = inventory_devices.update_devices_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {inventory_devices.base_url}{inventory_devices.endpoint}.")

    # assert PUT request
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # assert GET request
    with pytest.raises(requests.exceptions.RequestException):
        inventory_devices.get_devices()
