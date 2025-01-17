from test_support.helpers.api.base_api import BaseAPI
import requests


class EndpointInventoryDevices(BaseAPI):
    """
    Class for managing requests to 'inventory/devices' endpoint.
    Inherits from API.
    """
    @property
    def endpoint(self) -> str:
        """
        Endpoint for inventory devices.

        :return: The endpoint for requests towards Inventory devices.
        """
        return "/inventory/devices"

    def get_devices(self) -> requests.Response:
        """
        Retrieve the list of inventory devices.

        :return: The server's response containing the inventory devices.
        """
        return self._send_get_request(self.endpoint)

    def update_devices_and_status_code(self, body: dict) -> requests.Response:
        """
        Update the list of inventory devices and status code of GET request.

        :param body: A dictionary containing two keys:
            (1) body: list of devices
            (2) status_code: new status code for GET request.
        :return: The server's response to the update request.
        """
        return self._send_put_request(self.endpoint, body)
