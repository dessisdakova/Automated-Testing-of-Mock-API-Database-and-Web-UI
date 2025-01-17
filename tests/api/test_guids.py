from tests.api.fixtures import *
from test_support.common.yaml_loaders import load_api_test_data
from test_support.helpers.api.assertions import Assertions
import requests
import json


def test_get_request_retrieving_guids_list(guids, api_logger):
    """
    Test that a GET request retrieves the guid list successfully.
    """
    # arrange
    expected_values = []

    # act
    get_response = guids.get_guids()
    api_logger.debug(f"Sending a GET request to {guids.base_url}{guids.endpoint}.")

    # assert
    Assertions.assert_status_code(get_response, 200)
    Assertions.assert_response_is_json(get_response)
    Assertions.assert_guids_list_and_its_values(get_response, expected_values)


@pytest.mark.parametrize("value", ["7777", "sometext", "123!abc", "77.77", "77-+/!^_+77"])
def test_post_request_adding_valid_value_to_guids_list(add_guid, value, api_logger):
    """
    Test that a POST request adds guid values to the guids list successfully.
    """
    # arrange
    add_guid.guid = value
    api_logger.debug(f"GUID value: {add_guid.guid}")
    expected_list_of_values = [value]

    # act
    post_response = add_guid.add_guid_to_list()
    api_logger.debug(f"Sending a POST request to {add_guid.base_url}{add_guid.endpoint}.")

    # assert
    Assertions.assert_status_code(post_response, 200)
    Assertions.assert_response_is_json(post_response)
    Assertions.assert_guids_list_and_its_values(post_response, expected_list_of_values)


@pytest.mark.parametrize("value", ["#", "/", "", "?"])
def test_post_request_adding_invalid_value_to_guids_list(add_guid, value, api_logger):
    """
    Test that a POST request fails to add some special characters to the guids list.
    """
    # arrange
    add_guid.guid = value
    api_logger.debug(f"GUID value: {add_guid.guid}")

    # act
    post_response = add_guid.add_guid_to_list()
    api_logger.debug(f"Sending a POST request to {add_guid.base_url}{add_guid.endpoint}.")

    # assert
    Assertions.assert_not_found_response(post_response)


@pytest.mark.parametrize("test_data", load_api_test_data("api_guids")["Different_types"])
def test_put_request_change_response_of_get_request(guids, test_data, api_logger):
    """
    Test that a PUT request with different types of keys
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
    put_response = guids.update_guids_and_status_code(body)
    api_logger.debug(f"Sending a POST request to {guids.base_url}{guids.endpoint}.")
    get_response = guids.get_guids()
    api_logger.debug(f"Sending a GET request to {guids.base_url}{guids.endpoint}.")

    # assert PUT request
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # assert GET request
    Assertions.assert_get_response_matches_put_request(get_response, put_response)


@pytest.mark.parametrize("test_data", load_api_test_data("api_guids")["Status_code_valid_number"])
def test_put_request_change_response_of_get_request(guids, test_data, api_logger):
    """
    Test that a PUT request with different types of keys
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
    put_response = guids.update_guids_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {guids.base_url}{guids.endpoint}.")
    get_response = guids.get_guids()
    api_logger.debug(f"Sending a GET request to {guids.base_url}{guids.endpoint}.")

    # assert PUT request
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # assert GET request
    Assertions.assert_get_response_matches_put_request(get_response, put_response)


@pytest.mark.parametrize("test_data", load_api_test_data("api_guids")["Status_code_object"])
def test_behavior_when_status_code_is_sent_as_an_object(guids, test_data, api_logger):
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
    put_response = guids.update_guids_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {guids.base_url}{guids.endpoint}.")
    get_response = guids.get_guids()
    api_logger.debug(f"Sending a GET request to {guids.base_url}{guids.endpoint}.")

    # assert PUT request
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # assert GET request
    Assertions.assert_get_response_matches_put_request(get_response, put_response)


@pytest.mark.parametrize("test_data", load_api_test_data("api_guids")["Missing_key"])
def test_put_request_when_key_is_missing(guids, test_data, api_logger):
    """
    Test that a PUT request missing required key returns 500 Internal Server Error.
    """
    # arrange
    body = test_data
    api_logger.debug(f"Request body:\n{json.dumps(body, indent=4)}")

    # act
    put_response = guids.update_guids_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {guids.base_url}{guids.endpoint}.")

    # assert
    Assertions.assert_internal_server_error_response(put_response)


def test_put_request_when_body_is_missing(guids, api_logger):
    """
    Test that a PUT request with missing body returns 400 Bad Request.
    """
    # act
    put_response = guids.update_guids_and_status_code(body=None)
    api_logger.debug(f"Sending a PUT request to {guids.base_url}{guids.endpoint}.")

    # assert
    Assertions.assert_status_code(put_response, 400)


@pytest.mark.parametrize("test_data", load_api_test_data("api_guids")["Status_code_array_float"])
def test_behavior_when_status_code_is_sent_as_an_array_or_float(guids, test_data, api_logger):
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
    put_response = guids.update_guids_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {guids.base_url}{guids.endpoint}.")
    get_response = guids.get_guids()
    api_logger.debug(f"Sending a GET request to {guids.base_url}{guids.endpoint}.")

    # assert
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # response of GET request is 500 Internal Server Error
    Assertions.assert_internal_server_error_response(get_response)


@pytest.mark.parametrize("test_data", load_api_test_data("api_guids")["Status_code_invalid_string"])
def test_behavior_when_status_code_sent_as_invalid_string(guids, test_data, api_logger):
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
    put_response = guids.update_guids_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {guids.base_url}{guids.endpoint}.")

    # assert PUT request
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # a GET request can not be sent
    with pytest.raises(requests.exceptions.RequestException):
        guids.get_guids()


@pytest.mark.parametrize("test_data", load_api_test_data("api_guids")["Status_code_invalid_number"])
def test_behavior_when_status_code_is_an_integer_with_invalid_code(guids, test_data, api_logger):
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
    put_response = guids.update_guids_and_status_code(body)
    api_logger.debug(f"Sending a PUT request to {guids.base_url}{guids.endpoint}.")

    # assert PUT request
    Assertions.assert_status_code(put_response, 200)
    Assertions.assert_response_is_json(put_response)
    Assertions.assert_put_request_response_keys(put_response, body, expected_keys)
    # a GET request can not be sent
    with pytest.raises(requests.exceptions.RequestException):
        guids.get_guids()
