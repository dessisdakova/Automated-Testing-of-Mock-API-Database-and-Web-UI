from test_support.helpers.api.base_api import BaseAPI
import requests


class EndpointRootCerts(BaseAPI):
    """
    Class for retrieving the root certificates from '/mock_certs/root_ca' endpoint.
    Inherits from API.
    """
    @property
    def endpoint(self) -> str:
        """
        Endpoint for root certificates.

        :return: The endpoint for requests towards Root Certificates.
        """
        return "/mock_certs/root_ca"

    def get_root_certificates(self) -> requests.Response:
        """
        Retrieve the root certificates.

        :return: The server's response containing the certificates.
        """
        return self._send_get_request(self.endpoint)
