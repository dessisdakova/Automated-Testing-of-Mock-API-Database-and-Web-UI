from test_support.helpers.api.base_api import BaseAPI
import requests


class EndpointIntermediateCertificates(BaseAPI):
    """
    Class for retrieving the intermediate certificates from '/mock_certs/intermediate_ca' endpoint.
    Inherits from API.
    """

    @property
    def endpoint(self) -> str:
        """
        Endpoint for intermediate certificates.

        :return: The endpoint for requests towards Intermediate Certificates.
        """
        return "/mock_certs/root_ca"

    def get_intermediate_certificates(self) -> requests.Response:
        """
        Retrieve the intermediate certificates.

        :return: The server's response containing the certificates.
        """
        return self._send_get_request(self.endpoint)
