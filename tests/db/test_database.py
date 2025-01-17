from tests.db.fixtures import *
from test_support.common.yaml_loaders import load_db_test_data


@pytest.mark.parametrize("test_data", load_db_test_data("db_test_data")["queries"])
def test_provided_queries(db_connection, test_data, db_logger):
    # arrange
    query = test_data["query"]
    db_logger.debug(f"Query for execution: {query}.")
    expected = [tuple(row) for row in test_data["expected_results"]]
    db_logger.debug(f"Executed query for '{test_data['description']}'.")

    # act
    actual = db_connection.execute_query(query)

    # assert
    assert expected == actual

