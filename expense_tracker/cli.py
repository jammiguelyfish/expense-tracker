import click
from .models import Expense
from .sqlite_backend import SQLiteStorage
from .csv_backend import CSVStorage
from datetime import datetime


def _get_storage(storage_type, path):
    if storage_type == 'sqlite':
        return SQLiteStorage(path)
    return CSVStorage(path)


@click.group()
@click.option('--backend', type=click.Choice(['sqlite', 'csv']), default='sqlite')
@click.option('--path', default='data/expenses.db')
@click.pass_context
def cli(ctx, backend, path):
    ctx.ensure_object(dict)
    ctx.obj['storage'] = _get_storage(backend, path)


@cli.command()
@click.option('--amount', required=True, type=float)
@click.option('--category', required=True)
@click.option('--date', default=None, help='YYYY-MM-DD (defaults to today)')
@click.option('--description', default='')
@click.pass_context
def add(ctx, amount, category, date, description):
    if date is None:
        date = datetime.utcnow().date().isoformat()
    exp = Expense(id=None, date=date, amount=amount, category=category, description=description)
    saved = ctx.obj['storage'].add_expense(exp)
    click.echo(f"Added expense id={saved.id} amount={saved.amount} date={saved.date} category={saved.category}")


@cli.command()
@click.pass_context
def list(ctx):
    rows = ctx.obj['storage'].list_expenses()
    for r in rows:
        click.echo(f"{r.id}\t{r.date}\t{r.amount:.2f}\t{r.category}\t{r.description}")


@cli.command()
@click.argument('expense_id', type=int)
@click.pass_context
def get(ctx, expense_id):
    try:
        r = ctx.obj['storage'].get_expense(expense_id)
        click.echo(f"{r.id}\t{r.date}\t{r.amount:.2f}\t{r.category}\t{r.description}")
    except KeyError as e:
        click.echo(str(e))


@cli.command()
@click.argument('expense_id', type=int)
@click.pass_context
def delete(ctx, expense_id):
    ok = ctx.obj['storage'].delete_expense(expense_id)
    if ok:
        click.echo(f"Deleted {expense_id}")
    else:
        click.echo(f"Not found: {expense_id}")


if __name__ == '__main__':
    cli()
