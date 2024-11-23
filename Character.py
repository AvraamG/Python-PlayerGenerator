from GameMechanics import Class, GetHitDiceFromClass,Race,GetStatsFromRace,DiceVariants,CalculateModifier
from Stats import *
import random

#TODO Consider bringing stats here

class Character:

    Name:str
    Level:int
    Race:Race
    Class:Class
    Stats:Stats
    HPDice:DiceVariants
    HP:int

    def __init__(self, newName:str,newLevel:int,newRace:Race, newClass:Class, newStats:Stats):
        self.Name=newName
        self.Level=newLevel
        self.Race=newRace
        self.Class=newClass
        self.Stats= newStats
        self.HPDice = GetHitDiceFromClass(self.Class)
        self.HP = self.CalculateHP()
        self.AdjustStatsFromRace()

        print(f"{self.Name} was created. A level: {self.Level} {self.Race} {self.Class}with stats \n"
              f" STR: {self.Stats.Strength} \n"
              f" DEX: {self.Stats.Dexterity} \n"
              f" CON: {self.Stats.Constitution} \n"
              f" INT: {self.Stats.Intelligence} \n"
              f" WIS: {self.Stats.Wisdom} \n"
              f" CHA: {self.Stats.Charisma} \n"
              f"and HP:{self.HP} \n")

    def TakeDamage(self, damage):
        self.HP = self.HP - damage
        print(f"{self.Name} took {damage} points of damage. Remaining HP: {self.HP}")

    def Attack(self, target):
        damage = self.Stats.Strength/2
        print(f"{self.Name} attacked {target.Name} for {damage} points of damage")
        target.TakeDamage(damage)

    def CalculateHP(self) ->int:
        #At level 1 you get the maximum Hit dice + constitution modifier
        #For any other level you have to roll the Dice + constitution modifier.
        hpLevel1 = self.HPDice.value +CalculateModifier(self.Stats.Constitution)
        hp=hpLevel1
        additionalLevels= self.Level-1
        for everyNewLevel in range(additionalLevels):
            hp+= random.randint(1,self.HPDice.value) + CalculateModifier(self.Stats.Constitution)

        return hp

    def AdjustStatsFromRace(self):
        self.Stats += GetStatsFromRace(self.Race)
