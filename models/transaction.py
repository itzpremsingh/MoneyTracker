from dataclasses import dataclass
from datetime import date

@dataclass
class Transaction:
    transactionID: int
    transactionDate: date
    description: str
    amount: int
    transactionType: str
    balance: int
