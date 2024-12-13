from ItemFiles.EquipmentSlot import EquipmentSlot

class Item:
    def __init__(self, name: str, slot: EquipmentSlot, weight: float):
        self.Name = name
        self.Slot = slot
        self.Weight = weight
