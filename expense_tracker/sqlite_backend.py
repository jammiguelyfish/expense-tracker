import sqlite3
import os
from typing import List
from .storage import Storage
from .models import Expense


class SQLiteStorage(Storage):
    def __init__(self, path: str):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.conn = sqlite3.connect(self.path, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        cur = self.conn.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        )
        ''')
        self.conn.commit()

    def add_expense(self, expense: Expense) -> Expense:
        cur = self.conn.cursor()
        cur.execute('INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)', (expense.date, expense.amount, expense.category, expense.description))
        self.conn.commit()
        expense.id = cur.lastrowid
        return expense

    def list_expenses(self) -> List[Expense]:
        cur = self.conn.cursor()
        cur.execute('SELECT id, date, amount, category, description FROM expenses ORDER BY date DESC')
        rows = cur.fetchall()
        return [Expense(id=r[0], date=r[1], amount=r[2], category=r[3], description=r[4] or '') for r in rows]

    def get_expense(self, expense_id: int) -> Expense:
        cur = self.conn.cursor()
        cur.execute('SELECT id, date, amount, category, description FROM expenses WHERE id=?', (expense_id,))
        row = cur.fetchone()
        if not row:
            raise KeyError(f"Expense {expense_id} not found")
        return Expense(id=row[0], date=row[1], amount=row[2], category=row[3], description=row[4] or '')

    def delete_expense(self, expense_id: int) -> bool:
        cur = self.conn.cursor()
        cur.execute('DELETE FROM expenses WHERE id=?', (expense_id,))
        self.conn.commit()
        return cur.rowcount > 0
