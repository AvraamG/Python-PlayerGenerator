from GameMechanics import Class, GetHitDiceFromClass, Race, GetStatsFromRace, DiceVariants, CalculateModifier,DiceMethods

from Skill import Skill
from Stats import *

#TODO Consider bringing stats here

class Character:

    Name:str
    Level:int
    Race:Race
    Class:Class
    Stats:Stats
    HPDice:DiceVariants
    HP:int
    Skills:list[Skill]
    Initiative:int

    def __init__(self, newName:str,newLevel:int,newRace:Race, newClass:Class, newStats:Stats):
        self.Name:str=newName
        self.Level:int=newLevel
        self.Race:Race=newRace
        self.Class:Class=newClass
        self.Stats:Stats= newStats
        self.HPDice:DiceVariants = GetHitDiceFromClass(self.Class)
        self.HP:int = self.CalculateHP()
        self.AdjustStatsFromRace()
        #TODO implement the basic skills like Attack, Fortify,Run and maybe add some special skills from Class or Race
        self.Initiative = 0

        print(f"------- {self.Name} was created. A level: {self.Level} {self.Race.name} {self.Class.name} with stats ------- \n"
              f" STR: {self.Stats.Strength} \n"
              f" DEX: {self.Stats.Dexterity} \n"
              f" CON: {self.Stats.Constitution} \n"
              f" INT: {self.Stats.Intelligence} \n"
              f" WIS: {self.Stats.Wisdom} \n"
              f" CHA: {self.Stats.Charisma} \n"
              f" and HP:{self.HP} \n")

    def TakeDamage(self, damage):
        self.HP = self.HP - damage
        print(f"{self.Name} took {damage} points of damage. Remaining HP: {self.HP}")

    def Attack(self, target):
        damage = self.Stats.Strength/2
        print(f"{self.Name} attacked {target.Name} for {damage} points of damage")
        target.TakeDamage(damage)

    def RollForInitiative(self):
        roll = DiceMethods.RollDice(DiceVariants.D20)
        dexterityModifier = CalculateModifier(self.Stats.Dexterity)
        self.Initiative = roll + dexterityModifier
        print(f"{self.Name} has rolled {roll} and has Dexterity modifier: {dexterityModifier}. Total initiative score = {self.Initiative}")
        return roll + self.Initiative

    def CalculateHP(self) ->int:
        #At level 1 you get the maximum Hit dice + constitution modifier
        #For any other level you have to roll the Dice + constitution modifier.
        hpLevel1 = self.HPDice.value +CalculateModifier(self.Stats.Constitution)
        hp=hpLevel1
        additionalLevels= self.Level-1
        for everyNewLevel in range(additionalLevels):
            hp += DiceMethods.RollDice(self.HPDice) + CalculateModifier(self.Stats.Constitution)

        return hp

    def AdjustStatsFromRace(self):
        self.Stats += GetStatsFromRace(self.Race)
