from enum import Enum
import random
from CharacterFiles.Stats import Stats

class DiceVariants(Enum):
    D4=4
    D6=6
    D8=8
    D10=10
    D12=12
    D20=20
    D100=100

#TODO consider splitting this file to more parts
class Class(Enum):
    Barbarian=1
    Fighter=2
    Rogue=3
    Cleric=4
    Bard = 5

class Race(Enum):
    Human=1
    Elf=2
    Dwarf=3
    Halfling=4
    Gnome=5
    HalfElf=6
    HalfOrc=7
    HalfDrow=8
    Goblin = 9
    Orc = 10,

class DiceMethods:
    def RollDice(dice:DiceVariants):
       return random.randint(1, dice.value)

def CalculateModifier(ability_score: int) -> int:
    return (ability_score - 10) // 2

def GetHitDiceFromClass(someClass:Class) -> DiceVariants:
    match someClass:
        case Class.Barbarian:
            return DiceVariants.D12
        case Class.Fighter:
            return DiceVariants.D10
        case Class.Rogue:
            return DiceVariants.D6
        case Class.Cleric:
            return DiceVariants.D8
        case Class.Bard:
            return DiceVariants.D6
        case _:
            return DiceVariants.D6


def GetStatsFromRace(someRace:Race) -> Stats:

    match someRace:
        case Race.Human:
            return Stats(0,0,0,0,0,0)
        case Race.Elf:
            return Stats(0, 2, -2, 0, 0, 0)
        case Race.Halfling:
            return Stats(-2, +2, 0, 0, 0, 0)
        case Race.Gnome:
            return Stats(-2, 0, +2, 0, 0, 0)
        case Race.HalfElf:
            return Stats(0, 0, 0, 0, 0, 0)
        case Race.HalfOrc:
            return Stats(2, 0, 0, -2, 0, -2)
        case Race.HalfDrow:
            return Stats(0, 2, -2, 0, 0, 0)
        case Race.Goblin:
            return Stats(-2, 2, -2, -2, -2, -2)
        case Race.Orc:
            return Stats(2, 0, 2, -2, -2, 0)
        case _:
            return Stats(0, 0, 0, 0, 0, 0)


