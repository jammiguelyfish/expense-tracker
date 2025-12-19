from flask import Flask, render_template, request, redirect, url_for, jsonify
from .sqlite_backend import SQLiteStorage
from .models import Expense
from datetime import datetime

def create_app(db_path='data/web_expenses.db'):
    app = Flask(__name__)
    storage = SQLiteStorage(db_path)

    @app.route('/')
    def index():
        expenses = storage.list_expenses()
        total = sum(e.amount for e in expenses)
        return render_template('index.html', expenses=expenses, total=total)

    @app.route('/add', methods=['POST'])
    def add():
        amount = float(request.form['amount'])
        category = request.form['category']
        date = request.form.get('date') or datetime.utcnow().date().isoformat()
        description = request.form.get('description','')
        exp = Expense(id=None, date=date, amount=amount, category=category, description=description)
        storage.add_expense(exp)
        return redirect(url_for('index'))

    @app.route('/delete/<int:expense_id>', methods=['POST'])
    def delete(expense_id):
        storage.delete_expense(expense_id)
        return redirect(url_for('index'))

    @app.route('/api/expenses')
    def api_list():
        return jsonify([e.to_dict() for e in storage.list_expenses()])

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
