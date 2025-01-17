from test_support.common.yaml_loaders import load_config
import requests


class BaseAPI:
    """
    Base class for interacting with the server.
    Provides methods for sending requests and properties to configure and construct API base URL and certificates.
    """
    def __init__(self):
        """
        Initializes the API class by loading configuration.
        """
        self.config = load_config("api_config")

    @property
    def base_url(self) -> str:
        """
        Constructs and returns the base URL based on the configuration.

        :return: The base URL of the server.
        """
        protocol = "https" if self.config["use_https"] else "http"
        port = "443" if self.config["use_https"] else "80"
        return f"{protocol}://{self.config['api_host']}:{port}"

    @property
    def certificates(self) -> str or None:
        """
        Sets certificates based on protocol type - HTTPS or HTTP.

        :return: The certificates file path as a string if using HTTPS, or None
                 if using HTTP.
        """
        if self.config["use_https"]:
            return self.config["cert_file"]
        else:
            return None

    def _send_get_request(self, endpoint: str, headers: dict = None) -> requests.Response:
        """
        Send a GET request to the specified endpoint.

        :param endpoint: The API endpoint (relative to the base URL).
        :param headers: Optional headers for the request.
        :return: The server's response to the GET request.
        """
        return requests.get(self.base_url + endpoint, headers=headers, verify=self.certificates)

    def _send_put_request(self, endpoint: str, body: dict, headers: dict = None) -> requests.Response:
        """
        Send a PUT request to the specified endpoint.

        :param endpoint: The API endpoint (relative to the base URL).
        :param body: The JSON payload for the PUT request.
        :param headers: Optional headers for the request.
        :return: The server's response to the PUT request.
        """
        return requests.put(self.base_url + endpoint, headers=headers, json=body, verify=self.certificates)

    def _send_post_request(self, endpoint: str, files: dict = None, headers: dict = None) -> requests.Response:
        """
        Send a POST request to the specified endpoint.

        :param endpoint: The API endpoint (relative to the base URL).
        :param files: Files to upload with the POST request.
        :param headers: Optional headers for the request.
        :return: The server's response to the POST request.
        """
        return requests.post(self.base_url + endpoint, headers=headers, files=files, verify=self.certificates)
