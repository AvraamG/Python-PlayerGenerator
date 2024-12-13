from typing import List, Optional
from ItemFiles.Item import Item

class Bag:
    def __init__(self, max_weight: float):
        self.items: List[Item] = []
        self.max_weight = max_weight

    def add_item(self, item: Item) -> bool:
        if self.current_weight() + item.weight <= self.max_weight:
            self.items.append(item)
            return True
        else:
            print(f"Cannot add {item.name}. Bag is too heavy!")
            return False

    def remove_item(self, item: Item) -> Optional[Item]:
        if item in self.items:
            self.items.remove(item)
            return item
        return None

    def current_weight(self) -> float:
        return sum(item.weight for item in self.items)

    def list_items(self):
        return self.items
