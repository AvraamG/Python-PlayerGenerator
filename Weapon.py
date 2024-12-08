from Item import Item


class Weapon(Item):
    def __init__(self,damage:int,value:int):
        self.damage =damage
        #I should probably find a formula for calculating the value
        super().__init__(value)
        #Add what type of slot connection it has
