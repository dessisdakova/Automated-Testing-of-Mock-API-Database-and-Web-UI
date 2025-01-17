from test_support.PATHS import *
from datetime import datetime
import logging


def create_logger(logger_name: str, log_file_prefix: str) -> logging.Logger:
    """
    Creates and configures a custom logger for managing test logs.
    The logger stores logs in the "test_logs" folder with a custom format.
    A new log file is created each time the logger is initialized.

    :param logger_name: Name of the logger instance.
    :param log_file_prefix: Prefix for the log file name (e.g., "api_tests").
    :return: Configured logger instance.
    """
    # create a Logger instance
    logger = logging.Logger(logger_name, logging.DEBUG)

    # create a unique log file name with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_name = f"{log_file_prefix}_{timestamp}.log"

    # set path for save
    log_file_path = LOGS_DIRECTORY / log_file_name

    # create a file handler and a formatter
    file_handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter("%(asctime)s | %(levelname)-5s | %(message)s", datefmt="%Y/%m/%d %H:%M:%S")

    # attach formatter to handler
    file_handler.setFormatter(formatter)

    # attach handler to logger
    logger.addHandler(file_handler)

    return logger

