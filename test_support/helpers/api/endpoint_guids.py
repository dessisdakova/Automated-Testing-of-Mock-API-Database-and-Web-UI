from test_support.helpers.api.base_api import BaseAPI
import requests


class EndpointGuids(BaseAPI):
    """
    Class for managing requests to '/guids' endpoint.
    Inherits from API.
    """
    @property
    def endpoint(self) -> str:
        """
        Endpoint for guids.

        :return: The endpoint for requests towards Guids.
        """
        return "/guids"

    def get_guids(self) -> requests.Response:
        """
        Retrieve the list of guids.

        :return: The server's response containing the guids.
        """
        return self._send_get_request(self.endpoint)

    def update_guids_and_status_code(self, body: dict) -> requests.Response:
        """
        Update the list of guids and the status code of GET request.

        :param body: A dictionary containing two keys:
            body: list of guids
            status_code: new status code for GET request.
        :return: The server's response to the update request.
        """
        return self._send_put_request(self.endpoint, body)
