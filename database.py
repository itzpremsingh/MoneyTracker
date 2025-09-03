from sqlite3 import connect, Cursor, Connection

def getConnection() -> tuple[Connection, Cursor]:
    connection = connect(".database.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Money (
            transactionID INTEGER PRIMARY KEY AUTOINCREMENT,
            transactionDate DATE,
            description VARCHAR(100),
            amount INTEGER,
            transactionType TEXT CHECK(transactionType IN ('credit', 'debit')),
            balance INTEGER
        )
        """
    )

    return connection, cursor
