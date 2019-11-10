from masonite.helpers import config
from masonite.validation import BaseValidation


class not_in_database(BaseValidation):
    """ Takes a table name and column name and check if it exists
        in the database.
    """

    def __init__(
        self, validations, table, column, connection="", messages={}, raises={}
    ):
        """

        :param validations: From parent class
        :param table:   The table name
        :param column:  The column name
        :param connection:  The connection
        """
        super().__init__(validations, messages, raises)
        self.table = table
        self.column = column
        self.connection = connection or config("database.databases.default")

    def passes(self, attribute, key, dictionary):
        """
        Passes if cannot find value in database using provided table, column, and connection.
        """
        return (
            config("database.DB")
            .connection(self.connection)
            .table(self.table)
            .where(self.column, attribute)
            .first()
            is None
        )

    def message(self, key):
        return "{} already exists".format(key)

    def negated_message(self, key):
        return "{} does not exist".format(key)
