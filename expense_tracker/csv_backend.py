import csv
import os
from typing import List
from .storage import Storage
from .models import Expense


class CSVStorage(Storage):
    def __init__(self, path: str):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'date', 'amount', 'category', 'description'])
                writer.writeheader()

    def _read_all(self) -> List[dict]:
        with open(self.path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def _write_all(self, rows: List[dict]):
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'date', 'amount', 'category', 'description'])
            writer.writeheader()
            writer.writerows(rows)

    def add_expense(self, expense: Expense) -> Expense:
        rows = self._read_all()
        next_id = 1 + max((int(r['id']) for r in rows), default=0)
        row = {'id': str(next_id), 'date': expense.date, 'amount': f"{expense.amount:.2f}", 'category': expense.category, 'description': expense.description}
        rows.append(row)
        self._write_all(rows)
        expense.id = next_id
        return expense

    def list_expenses(self) -> List[Expense]:
        rows = self._read_all()
        return [Expense(id=int(r['id']), date=r['date'], amount=float(r['amount']), category=r['category'], description=r.get('description','')) for r in rows]

    def get_expense(self, expense_id: int) -> Expense:
        rows = self._read_all()
        for r in rows:
            if int(r['id']) == expense_id:
                return Expense(id=expense_id, date=r['date'], amount=float(r['amount']), category=r['category'], description=r.get('description',''))
        raise KeyError(f"Expense {expense_id} not found")

    def delete_expense(self, expense_id: int) -> bool:
        rows = self._read_all()
        new_rows = [r for r in rows if int(r['id']) != expense_id]
        if len(new_rows) == len(rows):
            return False
        self._write_all(new_rows)
        return True
