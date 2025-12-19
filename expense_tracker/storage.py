from abc import ABC, abstractmethod
from typing import List
from .models import Expense


class Storage(ABC):
    @abstractmethod
    def add_expense(self, expense: Expense) -> Expense:
        raise NotImplementedError

    @abstractmethod
    def list_expenses(self) -> List[Expense]:
        raise NotImplementedError

    @abstractmethod
    def get_expense(self, expense_id: int) -> Expense:
        raise NotImplementedError

    @abstractmethod
    def delete_expense(self, expense_id: int) -> bool:
        raise NotImplementedError
