from Item import Item

#Head slot
#Necklace slot
# 2 Ring slots
# Armor slot
# 2 Weapon slots (Mainhand and offhand) a 2 handed weapon takes both.

#TODO break this into 2 classes 1 for the things you can carry in your bag 1 for the things for equipment slots

class Inventory:
    def __init__(self,items:list[Item]):
        self.items = items