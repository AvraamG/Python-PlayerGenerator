from Character import Character
from Systems.GameMechanics import Class,Race
from Stats import *

class Player(Character):
    def __init__(self, newName:str,newLevel:int,newRace:Race, newClass:Class, newStats:Stats):
        super().__init__(newName,newLevel,newRace,newClass, newStats,False)

    def TakeDamage(self, damage):
        super().TakeDamage(damage)
