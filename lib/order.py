from dataclasses import dataclass
from datetime import date

# Using dataclass decorator - no need for init, eq and repr - done 
# automatically 
@dataclass
class Order:
    id: int
    customer_name: str 
    order_date: date
    