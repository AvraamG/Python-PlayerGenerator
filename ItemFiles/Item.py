from ItemFiles.EquipmentSlot import EquipmentSlot

class Item:
    def __init__(self, name: str, slot: EquipmentSlot, weight: float):
        self.name = name
        self.slot = slot
        self.weight = weight
