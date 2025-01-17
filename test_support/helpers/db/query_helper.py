from test_support.helpers.db.database_helper import DatabaseHelper
from typing import List


class QueryHelper(DatabaseHelper):
    """
    Helper class for executing database queries and handling query-related operations.
    Inherits from DatabaseHelper.
    """

    def execute_query(self, query: str) -> List[tuple]:
        """
        Execute a SQL query and fetch all results.

        :param query: The SQL query to execute.
        :return: List of tuples returned by the query.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
