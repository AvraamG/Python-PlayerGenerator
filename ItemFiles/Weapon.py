from ItemFiles.EquipmentSlot import EquipmentSlot
from ItemFiles.Item import Item
from SystemsFiles.GameMechanics import DiceVariants


class Weapon(Item):
    DamageRoll:DiceVariants
    def __init__(self,name:str,damageRoll:DiceVariants,weight:float):
        self.DamageRoll =damageRoll
        #I should probably find a formula for calculating the value
        super().__init__(name, EquipmentSlot.MainHandWeapon,weight )
        #Add what type of slot connection it has
