from argparse import ArgumentParser
from services.transaction_service import insertTransaction, getLastBalance, listTransactions

def runCLI(cursor) -> None:
    parser = ArgumentParser(description="Money Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # credit command
    parserCredit = subparsers.add_parser("credit", help="Add credit transaction")
    parserCredit.add_argument("amount", type=int)
    parserCredit.add_argument("description", type=str)

    # debit command
    parserDebit = subparsers.add_parser("debit", help="Add debit transaction")
    parserDebit.add_argument("amount", type=int)
    parserDebit.add_argument("description", type=str)

    # history
    parserHistory = subparsers.add_parser("history", help="Show history")
    parserHistory.add_argument("-r", "--range", type=int, default=10)

    # balance
    subparsers.add_parser("balance", help="Get balance")

    args = parser.parse_args()

    if args.command in ["credit", "debit"]:
        balance = getLastBalance(cursor)
        amount = args.amount
        if args.command == "debit":
            if amount > balance:
                print("Insufficient balance")
                return
            balance -= amount
        else:
            balance += amount

        insertTransaction(cursor, amount, args.description, args.command, balance)

    elif args.command == "balance":
        balance = getLastBalance(cursor)
        print(f"Balance: {balance}" if balance else "No transaction done")

    elif args.command == "history":
        listTransactions(cursor, args.range)

    else:
        parser.print_help()
