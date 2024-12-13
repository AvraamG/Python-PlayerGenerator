from typing import Optional
from ItemFiles.Bag import Bag
from ItemFiles.EquipmentSlot import EquipmentSlot
from ItemFiles.Item import Item

class Inventory:
    def __init__(self, bag_max_weight: float):
        self.EquippedItems: dict[EquipmentSlot, Optional[Item]] = {slot: None for slot in EquipmentSlot}
        self.Bag = Bag(bag_max_weight)
        self.CurrentEquippedWeight = 0.0

    def EquipItem(self, item: Item):
        slot = item.Slot
        if self.CurrentEquippedWeight + item.Weight > self.Bag.MaxCarryWeight:
            print(f"Cannot equip {item.Name}. Exceeds weight limit!")
            return
        if self.EquippedItems[slot]:
            self.Bag.AddItem(self.EquippedItems[slot])
            self.CurrentEquippedWeight -= self.EquippedItems[slot].Weight
        self.Bag.RemoveItem(item)
        self.EquippedItems[slot] = item
        self.CurrentEquippedWeight += item.Weight
        print(f"{item.Name} equipped to {slot.name}.")

    def UnEquipItem(self, slot: EquipmentSlot):
        if self.EquippedItems[slot]:
            item = self.EquippedItems[slot]
            if self.Bag.AddItem(item):
                self.CurrentEquippedWeight -= item.Weight
                self.EquippedItems[slot] = None
                print(f"{item.Name} unequipped from {slot.name}.")
            else:
                print(f"Cannot unequip {item.Name}, bag is too full!")
        else:
            print(f"No item is equipped in {slot.name}.")
