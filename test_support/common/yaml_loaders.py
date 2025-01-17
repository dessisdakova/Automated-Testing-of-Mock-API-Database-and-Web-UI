from test_support.PATHS import *
from pathlib import Path
from typing import Any
import yaml


def load_yaml(file_path: Path) -> Any:
    """
    An expandable method for loading YAML files from a folder and returning its contents as a Python object.

    :param file_path: Path to the YAML file.
    :return: Parsed content of the YAML file.
    """
    found_path = Path(file_path)
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    try:
        with open(found_path, "r") as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as error:
        raise ValueError(f"Invalid YAML in file {file_path}: {error}")


def load_config(file_name: str):
    """
    Load a configuration YAML file from 'test_config' folder.

    :param file_name: Name of the configuration file.
    :return: Parsed content of the YAML file.
    """
    if not file_name.endswith(".yaml"):
        file_name += ".yaml"
    file_path = CONFIG_DIRECTORY + file_name
    return load_yaml(file_path)


def load_api_test_data(file_name: str) -> Any:
    """
    Load a test data YAML file from the 'test_data/api' folder.

    :param file_name: Name of the test data file.
    :return: Parsed content of the YAML file.
    """
    if not file_name.endswith(".yaml"):
        file_name += ".yaml"
    file_path = TEST_DATA_API_DIRECTORY + file_name
    return load_yaml(file_path)


def load_db_test_data(file_name: str) -> Any:
    """
    Load a test data YAML file from the 'test_data/db' folder.

    :param file_name: Name of the test data file.
    :return: Parsed content of the YAML file.
    """
    if not file_name.endswith(".yaml"):
        file_name += ".yaml"
    file_path = TEST_DATA_DB_DIRECTORY + file_name
    return load_yaml(file_path)


def load_web_ui_test_data(file_name: str) -> Any:
    """
    Load a test data YAML file from the 'test_data/web_ui' folder.

    :param file_name: Name of the test data file.
    :return: Parsed content of the YAML file.
    """
    if not file_name.endswith(".yaml"):
        file_name += ".yaml"
    file_path = TEST_DATA_WEB_UI_DIRECTORY + file_name
    return load_yaml(file_path)
