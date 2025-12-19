from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional


@dataclass
class Expense:
    id: Optional[int]
    date: str  # ISO date
    amount: float
    category: str
    description: str = ""

    def to_dict(self):
        d = asdict(self)
        if self.id is None:
            d.pop('id')
        return d

