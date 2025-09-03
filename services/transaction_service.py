from datetime import datetime
from sqlite3 import Cursor
from utils.formatter import printTransaction


def insertTransaction(
    cursor: Cursor, amount: int, description: str, transactionType: str, balance: int
) -> None:
    cursor.execute(
        """
        INSERT INTO Money (transactionDate, description, amount, transactionType, balance)
        VALUES (?, ?, ?, ?, ?)
        """,
        (datetime.now().date(), description, amount, transactionType, balance),
    )

def getLastBalance(cursor: Cursor) -> int:
    cursor.execute("SELECT balance FROM Money ORDER BY transactionID DESC LIMIT 1")
    result = cursor.fetchone()
    return result[0] if result else 0

def fetchTransactions(cursor: Cursor, limit: int) -> list:
    cursor.execute(
        f"""
        SELECT transactionID, transactionDate, description, amount, transactionType, balance
        FROM Money
        ORDER BY transactionID DESC LIMIT {limit}
        """
    )
    return cursor.fetchall()

def listTransactions(cursor: Cursor, limit: int) -> None:
    records = fetchTransactions(cursor, limit)[::-1]
    if not records:
        print("No transaction done")
        return
    for record in records:
        printTransaction(record)
