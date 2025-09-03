# CLI Money Tracker

A simple command-line tool to track your income, expenses, and balance using SQLite.

---

## Features

- Add transactions (credit/debit) with descriptions.
- View transaction history (customizable range).
- Check current balance.
- Color-coded output for easy readability.
- Lightweight SQLite database for persistent storage.

---

## Installation

```bash
git clone https://github.com/<username>/cli-money-tracker.git
cd cli-money-tracker
python main.py
```

No external dependencies required.

---

## Usage

### Add a Transaction
```bash
python main.py add 500 "Salary" credit
python main.py add 200 "Groceries" debit
```

### View Balance
```bash
python main.py balance
```

### View Transaction History
```bash
python main.py history -r 10
```
- `-r` or `--range` defines how many recent transactions to show.

---

## Project Structure

```
cli-money-tracker/
├─ chat/
│  ├─ __init__.py
│  ├─ client.py
│  ├─ client_curses.py
│  ├─ helper.py
│  ├─ server.py
├─ main.py
└─ README.md
```

---

## License

MIT License
