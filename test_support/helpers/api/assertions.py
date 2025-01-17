import requests


class Assertions:
    @staticmethod
    def assert_status_code(response: requests.Response, expected: int) -> None:
        """
        Assert that the response status code matches the expected status code.

        :param response: The response object to validate.
        :param expected: The expected status code.
        :return: None.
        """
        assert response.status_code == expected, f"Response status code is {response.status_code}, expected {expected}."

    @staticmethod
    def assert_response_is_json(response: requests.Response) -> None:
        """
        Assert that the response body is either a JSON object or an array.

        :param response: The response object to validate.
        :return: None.
        """
        assert isinstance(response.json(), (list, dict)), "Response body is neither an object nor an array."

    @staticmethod
    def assert_keys_in_inventory_device(response: requests.Response, expected_keys: list) -> None:
        """
        Validate that the response contains specific keys in each device object.

        :param response: The response object to validate.
        :param expected_keys: List of top-level keys expected in each device.
        :return: None.
        """
        for device in response.json():
            for key in expected_keys:
                assert key in device, f"Key '{key}' is missing in device."

    @staticmethod
    def assert_sub_keys_for_key_in_inventory_device(response: requests.Response,
                                                    sub_key_name: str, expected_sub_keys: list) -> None:
        """
        Validate that each device object contains nested sub-keys in a specific key.

        :param response: The response object to validate.
        :param sub_key_name: Name of the sub-key in each device to validate.
        :param expected_sub_keys: List of keys expected within the sub-key.
        :return: None.
        """
        for device in response.json():
            sub_key = device.get(sub_key_name)
            assert sub_key is not None, f"Key '{sub_key_name}' is missing in device."
            assert isinstance(sub_key, dict), f"Key '{sub_key_name}' is not an object in device."
            for expected_sub_key in expected_sub_keys:
                assert expected_sub_key in sub_key, f"Sub-key '{expected_sub_key}' is missing in '{sub_key_name}'."

    @staticmethod
    def assert_guids_list_and_its_values(response: requests.Response, expected_values: list) -> None:
        """
        Validate that the response contains a 'guids' key, which is an array matching the expected values.

        :param response: The response object to validate.
        :param expected_values: List of expected values in the guids list.
        :return: None.
        """
        data = response.json()
        assert "guids" in data, "Key 'guids' is missing."
        assert len(data) == 1, "There are more than one keys."
        assert isinstance(data["guids"], list), "Key 'guids' is not array."
        assert data["guids"] == expected_values, "Key 'guids' values are not as expected."

    @staticmethod
    def assert_put_request_response_keys(response: requests.Response, body: dict, expected_keys: list) -> None:
        """
        Validate the response of a PUT request contains expected keys and matches the request body.

        :param response: The PUT response to validate.
        :param body: The request body sent in the PUT request.
        :param expected_keys: List of keys expected in the response.
        :return: None.
        """
        data = response.json()
        for key in expected_keys:
            assert key in data, f"Key '{key}' is missing in response."
        assert data["new_body"] == body["body"], "'body' keys don't match."
        assert data["new_status_code"] == body["status_code"], "'status_code' keys don't match."

    @staticmethod
    def assert_get_response_matches_put_request(get_response: requests.Response,
                                                put_response: requests.Response) -> None:
        """
        Validate that the GET response reflects changes made by a PUT request.

        :param get_response: The GET response to validate.
        :param put_response: The PUT response used for comparison.
        :return: None.
        """
        data = put_response.json()
        get_data = get_response.json()
        assert get_data == data["new_body"], "Body of GET request was not changed."
        try:
            new_status_code = int(data["new_status_code"])
            assert get_response.status_code == new_status_code, "Status code of GET request was not changed."
        except (ValueError, TypeError):
            # If the status_code is not valid, the server sets default status code ot GET request
            assert get_response.status_code == put_response.status_code, \
                "Status code should remain the same when 'new_status_code' is invalid."

    @staticmethod
    def assert_internal_server_error_response(response: requests.Response) -> None:
        """
        Assert that the response represents a 500 Internal Server Error.

        :param response: The response object to validate.
        :return: None.
        """
        assert response.status_code == 500, \
            f"Response status code is {response.status_code}, expected 500 Internal Server Error."
        assert "Internal Server Error" in response.text, "Response does not contain 'Internal Server Error'."
        assert response.headers.get("Content-Type", "").startswith("text/html"), "Response is not HTML."

    @staticmethod
    def assert_not_found_response(response: requests.Response) -> None:
        """
        Assert that the response represents a 404 Not Found error.

        :param response: The response object to validate.
        :return: None.
        """
        assert response.status_code == 404, f"Response status code is {response.status_code}, expected 404 NOT FOUND."
        assert "404 Not Found" in response.text, "Response does not contain '404 Not Found'."
        assert response.headers.get("Content-Type", "").startswith("text/html"), "Response is not HTML."

    @staticmethod
    def assert_response_when_retrieving_certificates(response: requests.Response) -> None:
        """
        Assert that the response includes the start and end of certificates,
        has an attachment and sends the certificates.

        :param response: The response object to validate.
        :return: None.
        """
        assert "-----BEGIN CERTIFICATE-----" in response.text, "Response does not contain start of certificates."
        assert "-----END CERTIFICATE-----" in response.text, "Response does not contain end of certificates."
        assert response.headers.get("Content-Disposition", "").startswith("attachment"), \
            "Response does not have an attachment."
        assert response.headers.get("Content-Type", "").startswith("application/pem-certificate-chain"), \
            "Response is not sending certificates."

    @staticmethod
    def assert_certificates_are_uploaded_to_container(response: requests.Response, file_name: str) -> None:
        """
        Assert that a certificate file was successfully uploaded to the container.

        :param response: The response object from the server.
        :param file_name: The name of the file expected to be uploaded.
        :return: None.
        """
        assert f"File uploaded successfully to /opt/project/upload/{file_name}" in response.text, \
            "File was not uploaded."

    @staticmethod
    def assert_file_is_missing_in_request(response: requests.Response) -> None:
        """
        Assert that the response indicates a file is missing in the request.

        :param response: The response object from the server.
        :return: None.
        """
        assert f"No file part in the request" in response.text, "Incorrect error message."

    @staticmethod
    def assert_file_is_not_selected_in_request(response: requests.Response) -> None:
        """
        Assert that the response indicates no file was selected in the request.

        :param response: The response object from the server.
        :return: None.
        """
        assert f"No selected file" in response.text, "Incorrect error message."
