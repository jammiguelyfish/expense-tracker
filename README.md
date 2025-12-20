# Expense Tracker

Simple expense tracker with CSV and SQLite backends and a small CLI with Web-based UI.

Requirements:

- Python 3.8+
- See `requirements.txt`

Quick start (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m expense_tracker.demo
```

CLI examples:

```powershell
python -m expense_tracker.cli add --amount 12.5 --category Coffee --description Morning
python -m expense_tracker.cli list
python -m expense_tracker.cli get 1
python -m expense_tracker.cli delete 1
```

