# Expense Tracker

Simple expense tracker with CSV and SQLite backends and a small CLI.

Requirements:


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
 
Web-based UI

This project also includes a lightweight web-based user interface built with Flask. The web UI lets you view all expenses, see the total, add new expenses using a simple form, and delete existing entries. There is also a JSON API endpoint that returns all expenses.

Features:

- **View expenses:** browse all stored expenses and see a running total.
- **Add expense:** submit a form with `amount`, `category`, `date` (optional), and `description`.
- **Delete expense:** remove an expense from the list.
- **API endpoint:** `GET /api/expenses` returns expense data as JSON.

Run the web UI (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m expense_tracker.webapp
```

The development server starts on http://127.0.0.1:5000 by default. The default SQLite database used by the web app is `data/web_expenses.db`; delete or move that file to reset the stored web UI data.

Files of interest:

- `expense_tracker/webapp.py` - Flask application and routes.
- `expense_tracker/templates/index.html` - HTML template for the web UI.
- `expense_tracker/static/style.css` - styles used by the web interface.

If you want to run the app with a different database path, modify `create_app()` in `expense_tracker/webapp.py` when creating the app, or run a small wrapper that passes a different `db_path`.
