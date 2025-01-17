from test_support.helpers.api.base_api import BaseAPI
import requests
from pathlib import Path


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
    def get_file_path(file_name: str) -> Path:
        """
        Get the file for uploading from test_data/ folder.

        :return: Path to file.
        """
        return Path(__file__).resolve().parent.parent.parent.parent / "test_data" / file_name

    def upload_file_to_server(self, files: dict = None) -> requests.Response:
        """
        Upload file to server.

        :return: The server's response for uploading file.
        """
        return self._send_post_request(self.endpoint, files=files)
