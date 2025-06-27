from dataclasses import dataclass

# Using dataclass decorator - no need for init, eq and repr - done 
# automatically 
@dataclass
class Item:
    id: int
    name: str 
    unit_price: int
    quantity: int 