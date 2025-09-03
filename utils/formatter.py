from datetime import datetime

def printTransaction(record: tuple) -> None:
    _, issuedDate, reason, amount, _type, balance = record
    dateObj = datetime.strptime(issuedDate, "%Y-%m-%d")
    date = f"{dateObj.day}-{dateObj.month}-{dateObj.year}"

    colorCode = "\033[92m" if _type == "credit" else "\033[91m"
    print(f"\nDate: \033[96m{date}\33[m")
    print(f"Amount  -> {amount} ({colorCode}{_type.title()}\033[0m)")
    print(f"Reason  -> {reason}")
    print(f"Balance -> {balance}")
