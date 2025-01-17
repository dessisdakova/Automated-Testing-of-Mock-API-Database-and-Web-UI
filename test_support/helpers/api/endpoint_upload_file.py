from test_support.helpers.api.base_api import BaseAPI
from test_support.PATHS import TEST_DATA_API_DIRECTORY
import requests


class EndpointUploadFile(BaseAPI):
    """
    Class for uploading files to the server using '/file/add' endpoint.
    Inherits from API.
    """

    @property
    def endpoint(self) -> str:
        """
        Endpoint for uploading files.

        :return: The endpoint for requests towards Upload File.
        """
        return "/file/add"

    @staticmethod
    def get_file_path(file_name: str) -> str:
        """
        Get the file for uploading from test_data/api folder.

        :return: Path to file represented in string format.
        """
        return TEST_DATA_API_DIRECTORY + file_name

    def upload_file_to_server(self, files: dict = None) -> requests.Response:
        """
        Upload file to server.

        :return: The server's response for uploading file.
        """
        return self._send_post_request(self.endpoint, files=files)
