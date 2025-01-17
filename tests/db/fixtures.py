from test_support.helpers.db.query_helper import QueryHelper
import pytest


@pytest.fixture(scope="session")
def db_connection(db_logger):
    """
    Fixture to provide a database connection using the QueryHelper.
    Establishes a connection at the start of the test session and closes it afterward.

    :param db_logger: Logger fixture for logging test events.
    """
    db = QueryHelper()
    db.connect()
    db_logger.info("Connection to the database is established.")
    yield db
    db.close()
    db_logger.info("Connection to the database is closed.")
