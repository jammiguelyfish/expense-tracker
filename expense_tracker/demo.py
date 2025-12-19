from .sqlite_backend import SQLiteStorage
from .csv_backend import CSVStorage
from .models import Expense
from datetime import datetime


def run_demo():
    print('Running demo...')
    sqlite = SQLiteStorage('data/demo_expenses.db')
    csvs = CSVStorage('data/demo_expenses.csv')

    e1 = Expense(id=None, date=datetime.utcnow().date().isoformat(), amount=12.5, category='Coffee', description='Morning')
    e2 = Expense(id=None, date=datetime.utcnow().date().isoformat(), amount=25.0, category='Groceries', description='Weekly')

    sqlite.add_expense(e1)
    sqlite.add_expense(e2)

    csvs.add_expense(Expense(id=None, date=e1.date, amount=e1.amount, category=e1.category, description=e1.description))

    print('SQLite entries:')
    for r in sqlite.list_expenses():
        print(r)

    print('CSV entries:')
    for r in csvs.list_expenses():
        print(r)


if __name__ == '__main__':
    run_demo()
