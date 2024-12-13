from typing import Optional
from ItemFiles.Bag import Bag
from ItemFiles.EquipmentSlot import EquipmentSlot
from ItemFiles.Item import Item

class Inventory:
    def __init__(self, bag_max_weight: float):
        self.equipped: dict[EquipmentSlot, Optional[Item]] = {slot: None for slot in EquipmentSlot}
        self.bag = Bag(bag_max_weight)
        self.equipped_weight = 0.0

    def equip_item(self, item: Item):
        slot = item.slot
        if self.equipped_weight + item.weight > self.bag.max_weight:
            print(f"Cannot equip {item.name}. Exceeds weight limit!")
            return
        if self.equipped[slot]:
            self.bag.add_item(self.equipped[slot])
            self.equipped_weight -= self.equipped[slot].weight
        self.bag.remove_item(item)
        self.equipped[slot] = item
        self.equipped_weight += item.weight
        print(f"{item.name} equipped to {slot.name}.")

    def unequip_item(self, slot: EquipmentSlot):
        if self.equipped[slot]:
            item = self.equipped[slot]
            if self.bag.add_item(item):
                self.equipped_weight -= item.weight
                self.equipped[slot] = None
                print(f"{item.name} unequipped from {slot.name}.")
            else:
                print(f"Cannot unequip {item.name}, bag is too full!")
        else:
            print(f"No item is equipped in {slot.name}.")
