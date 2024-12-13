from typing import List, Optional
from ItemFiles.Item import Item

class Bag:
    def __init__(self, max_weight: float):
        self.BagItems: List[Item] = []
        self.MaxCarryWeight = max_weight

    def AddItem(self, item: Item) -> bool:
        if self.CurrentWeight() + item.Weight <= self.MaxCarryWeight:
            self.BagItems.append(item)
            return True
        else:
            print(f"Cannot add {item.Name}. Bag is too heavy!")
            return False

    def RemoveItem(self, item: Item) -> Optional[Item]:
        if item in self.BagItems:
            self.BagItems.remove(item)
            return item
        return None

    def CurrentWeight(self) -> float:
        return sum(item.Weight for item in self.BagItems)

    def ListAllBagItems(self):
        return self.BagItems
