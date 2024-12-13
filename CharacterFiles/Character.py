#Thi is to resolve self referencing the CharacterFiles in the PickTarget. Arguably, Pick Target could be in the Combat System
from __future__ import annotations
import random
from typing import cast

from CharacterFiles.Stats import Stats
from ItemFiles.EquipmentSlot import EquipmentSlot
from ItemFiles.Item import Item
from ItemFiles.Weapon import Weapon
from SystemsFiles.GameMechanics import Class, GetHitDiceFromClass, Race, GetStatsFromRace, DiceVariants, CalculateModifier,DiceMethods
from ItemFiles.Inventory import Inventory


from SkillsFiles.Skill import Skill

#TODO Consider bringing stats here
#TODO bring an Act method that selects an action (E.g Fight, Heal, Run, Surrender) *Surrender sounds like a nice concept. The winner decides the fate. Eliminate, Release, Bring into the party.
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
    IsInCombat:bool
    IsEnemyToParty:bool
    Inventory:Inventory
    CanCarryMaxWeight:float

    def __init__(self, newName:str,newLevel:int,newRace:Race, newClass:Class, newStats:Stats,isEnemyToParty:bool):
        self.Name:str=newName
        self.Level:int=newLevel
        self.Race:Race=newRace
        self.Class:Class=newClass
        self.Stats:Stats= newStats
        self.HPDice:DiceVariants = GetHitDiceFromClass(self.Class)
        self.HP:int = self.CalculateHP()
        self.AdjustStatsFromRace()
        #TODO maybe add some special skills from Class or Race
        self.Initiative = 0
        self.IsInCombat = False
        self.IsEnemyToParty = isEnemyToParty
        self.Inventory = Inventory(CalculateModifier(self.Stats.Strength)*10 +100)



    def DebugPlayerStats(self):
        print(
            f"------- {self.Name} was created. A level: {self.Level} {self.Race.name} {self.Class.name} with stats ------- \n"
            f" STR: {self.Stats.Strength} \n"
            f" DEX: {self.Stats.Dexterity} \n"
            f" CON: {self.Stats.Constitution} \n"
            f" INT: {self.Stats.Intelligence} \n"
            f" WIS: {self.Stats.Wisdom} \n"
            f" CHA: {self.Stats.Charisma} \n"
            f" and HP:{self.HP} \n")



    def Attack(self, target):
        #TODO add attack Roll for Hit Miss
        #TODO add attack modifier based on class?
        damage = self.CalculateDamage()
        print(f"{self.Name} attacked {target.Name} for {damage} points of damage")
        target.TakeDamage(damage)

    def CalculateDamage(self) -> int:
        damage = CalculateModifier(self.Stats.Strength)
        main_hand_weapon = self.Inventory.EquippedItems.get(EquipmentSlot.MainHandWeapon)
        if main_hand_weapon:
            main_hand_weapon = cast(Weapon,main_hand_weapon)
            damage += DiceMethods.RollDice(main_hand_weapon.DamageRoll)
        return damage

    def TakeDamage(self, damage):
        self.HP = self.HP - damage
        print(f"{self.Name} took {damage} points of damage. Remaining HP: {self.HP}")
        if self.HP <= 0:
            self.Die()

    def Die(self):
        print(f"****** {self.Name} has died. ******")
        from SystemsFiles import CombatSystem
        CombatSystem.RemoveCharacterFromCombat(self)

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

    def PickTarget(self, allParticipants: list[Character]) -> Character:
        target: Character
        enemyParty = [character for character in allParticipants if character.IsEnemyToParty]
        playerParty = [character for character in allParticipants if not character.IsEnemyToParty]

        if self.IsEnemyToParty:
            target = random.choice(playerParty)
        else:
            target = random.choice(enemyParty)

        return target

    def AddItemToBag(self, item: Item):
        if self.Inventory.Bag.AddItem(item):
            print(f"{self.Name} added {item.Name} to their bag.")
        else:
            print(f"{self.Name} cannot add {item.Name}, bag is too heavy.")

    def EquipItem(self, item: Item):
        self.Inventory.EquipItem(item)

    def UnEquipItem(self, slot: EquipmentSlot):
        self.Inventory.UnEquipItem(slot)

"""
    def DisplayInventory(self):
        print(f"{self.Name}'s Inventory:")
        print("Equipped Items:")
        equipped = self.Inventory.list_equipped_items()
        for slot, item_name in equipped.items():
            print(f"  {slot}: {item_name if item_name else 'Empty'}")
        print("Bag Items:")
        for item in self.inventory.bag.list_items():
            print(f"  {item.name} (Weight: {item.weight})")
        print(f"Total Weight: {self.inventory.total_weight()}")
"""