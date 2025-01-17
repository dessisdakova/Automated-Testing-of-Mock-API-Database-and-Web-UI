from test_support.common.create_logger import create_logger
from test_support.helpers.api.endpoint_inventory_devices import EndpointInventoryDevices
from test_support.helpers.api.endpoint_guids import EndpointGuids
from test_support.helpers.api.endpoint_add_guid import EndpointAddGuids
from test_support.helpers.api.endpoint_root_certs import EndpointRootCerts
from test_support.helpers.api.endpoint_intermediate_certs import EndpointIntermediateCertificates
from test_support.helpers.api.endpoint_upload_file import EndpointUploadFile
from test_support.common.yaml_loaders import load_api_test_data
from test_support.common.yaml_loaders import load_config
import pytest
from typing import Generator


@pytest.fixture(scope="function", autouse=True)
def log_protocol(api_logger):
    is_protocol_https = load_config("api_config")["use_https"]
    if is_protocol_https:
        api_logger.info("Using HTTPS.")
    else:
        api_logger.info("Using HTTP.")


@pytest.fixture(scope="function")
def inventory_devices() -> EndpointInventoryDevices:
    """
    Provides an instance of InventoryDevices for interacting with 'inventory/devices' endpoint.

    :return: EndpointInventoryDevices instance.
    """
    return EndpointInventoryDevices()


@pytest.fixture(scope="function")
def guids() -> EndpointGuids:
    """
    Provides an instance of Guids for interacting with '/guids' endpoint.

    :return: EndpointGuids instance.
    """
    return EndpointGuids()


@pytest.fixture(scope="function")
def add_guid() -> EndpointAddGuids:
    """
    Provides an instance of AddGuids for interacting with '/{guid}/add' endpoint.

    :return: EndpointAddGuids instance.
    """
    return EndpointAddGuids()


@pytest.fixture(scope="function")
def root_certs() -> EndpointRootCerts:
    """
    Provides an instance of RootCertificates for interacting with '/mock_certs/root_ca' endpoint.

    :return: EndpointRootCerts instance.
    """
    return EndpointRootCerts()


@pytest.fixture(scope="function")
def intermediate_certs() -> EndpointIntermediateCertificates:
    """
    Provides an instance of IntermediateCertificates for interacting with '/mock_certs/intermediate_ca' endpoint.

    :return: EndpointIntermediateCertificates instance.
    """
    return EndpointIntermediateCertificates()


@pytest.fixture(scope="function")
def upload_file() -> EndpointUploadFile:
    """
    Provides an instance of UploadFile for interacting with '/file/add' endpoint.

    :return: EndpointUploadFile instance.
    """
    return EndpointUploadFile()


@pytest.fixture(scope="function", autouse=True)
def reset_server_state(inventory_devices, guids, api_logger) -> Generator[None, None, None]:
    """
    Resets the server state after each test to ensure isolation and prevent test dependency.

    The reset process involves:
    - Updating the inventory devices to their default state using initial data.
    - Updating the GUIDs to their default state using initial data.

    :param inventory_devices: Fixture to interact with 'inventory/devices' endpoint.
    :param guids: Fixture to interact with '/guids' endpoint.
    :param api_logger: Fixture to log tests.
    :yield: Allows test execution before resetting the state.
    """
    yield
    data = load_api_test_data("api_reset_sever")["reset"]
    body_inv = data["inventory"]

    body_guids = data["guids"]

    inventory_devices.update_devices_and_status_code(body_inv)
    guids.update_guids_and_status_code(body_guids)
    api_logger.info("Server is reset.")



