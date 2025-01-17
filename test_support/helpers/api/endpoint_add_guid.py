from test_support.helpers.api.base_api import BaseAPI
import requests


class EndpointAddGuids(BaseAPI):
    """
    Class for managing requests to '/{guid}/add' endpoint.
    Inherits from API.
    """
    def __init__(self):
        super().__init__()
        self._guid = None

    @property
    def guid(self) -> str:
        """
        Retrieve the current GUID value.

        :return: The GUID value as a string.
        """
        if self._guid is None:
            raise ValueError("GUID is not set. Please set a valid GUID before making a request.")
        return self._guid

    @guid.setter
    def guid(self, value: str):
        """
        Set or update the GUID value.

        :param value: The new GUID value.
        """
        self._guid = value

    @property
    def endpoint(self) -> str:
        """
        Endpoint for adding a guid.

        :return: The endpoint for adding a guid.
        """
        return f"/{self.guid}/add"

    def add_guid_to_list(self) -> requests.Response:
        """
        Add the current GUID to the list.

        :return: The server's response to the request.
        """
        return self._send_post_request(self.endpoint)
