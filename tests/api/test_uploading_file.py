from tests.api.fixtures import *
from test_support.helpers.api.assertions import Assertions


def test_uploading_file_successfully(upload_file, api_logger):
    """
    Test that a POST request uploads a file in the container successfully.
    """
    # arrange
    file_name = "upload_to_server.txt"
    file_path = upload_file.get_file_path(file_name)
    api_logger.debug(f"Selected file: {file_path}")

    # act
    # In order to send a file, it needs to be read and converted into a format that can be included in the request
    with open(file_path, "rb") as file:
        # files dictionary is a standard way of packaging files in requests
        files = {'file': (file_name, file, 'application/octet-stream')}

        # send the POST request with the file
        post_response = upload_file.upload_file_to_server(files=files)
        api_logger.debug(f"Sending a GET request to {upload_file.base_url}{upload_file.endpoint}.")

    # assert
    Assertions.assert_status_code(post_response, 200)
    Assertions.assert_certificates_are_uploaded_to_container(post_response, file_name)


def test_sending_request_without_attached_file(upload_file, api_logger):
    """
    Test that a POST request with missing file returns
    status code 400 Bad Request and correct corresponding error message 'No file part in the request'.
    """
    # act
    post_response = upload_file.upload_file_to_server()
    api_logger.debug(f"Sending a GET request to {upload_file.base_url}{upload_file.endpoint}.")

    # assert
    Assertions.assert_status_code(post_response, 400)
    Assertions.assert_file_is_missing_in_request(post_response)


def test_sending_request_without_selected_file(upload_file, api_logger):
    """
    Test that a POST request with no selected file returns
    status code 400 Bad Request and correct corresponding error message 'No selected file'.
    """
    # arrange
    files = {"file": ("", b"")}

    # act
    post_response = upload_file.upload_file_to_server(files=files)
    api_logger.debug(f"Sending a GET request to {upload_file.base_url}{upload_file.endpoint}.")

    # assert
    Assertions.assert_status_code(post_response, 400)
    Assertions.assert_file_is_not_selected_in_request(post_response)
