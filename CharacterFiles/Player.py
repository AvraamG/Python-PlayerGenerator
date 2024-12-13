from CharacterFiles.Character import Character
from CharacterFiles.Stats import Stats
from SystemsFiles.GameMechanics import Class,Race

class Player(Character):
    def __init__(self, newName:str,newLevel:int,newRace:Race, newClass:Class, newStats:Stats):
        super().__init__(newName,newLevel,newRace,newClass, newStats,False)

