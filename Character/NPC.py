from Character import Character
from Systems.GameMechanics import Class,Race
from Stats import *

class NPC(Character):
    def __init__(self, newName:str,newLevel:int,newRace:Race, newClass:Class, newStats:Stats):
        super().__init__(newName,newLevel,newRace,newClass, newStats,True)

    def TakeDamage(self, damage):
        super().TakeDamage(damage)


