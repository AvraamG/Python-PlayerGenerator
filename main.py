from CharacterFiles.Player import Player
from CharacterFiles.NPC import  NPC
from CharacterFiles.Stats import Stats
from ItemFiles.EquipmentSlot import EquipmentSlot
from ItemFiles.Item import Item
from ItemFiles.Weapon import Weapon
from SystemsFiles.GameMechanics import Class, Race, DiceVariants
from SystemsFiles.CombatSystem import GroupFight

def main():
   sword = Weapon("Sword of Power",DiceVariants.D10, 10.0)
   shield = Item("Shield of Valor", EquipmentSlot.OffHandWeapon, 15.0)
   helmet = Item("Helmet of Wisdom", EquipmentSlot.Head, 5.0)
   armor = Item("Plate Armor", EquipmentSlot.Armor, 30.0)

   #TODO start reading players and Encounters from Json
   Squee = Player("Squee",2,Race.Goblin,Class.Rogue,Stats.GenerateStatsAllTen())
   Squee.AddItemToBag(sword)
   Squee.EquipItem(sword)

   Needle = Player("Needle",3,Race.Halfling,Class.Bard,Stats(10,10,10,10,10,10))


   GoblinRogue = NPC("Goblin rogue",1,Race.Goblin,Class.Rogue,Stats(6,8,6,6,6,6))
   GoblinLackey = NPC("Goblin lackey",1,Race.Goblin,Class.Rogue,Stats(6,8,6,6,6,6))
   GoblinBoss = NPC("Goblin Boss",1,Race.Goblin,Class.Fighter,Stats(8,10,8,8,8,8))
   GoblinAmbusher = NPC("Goblin Ambusher",1,Race.Goblin,Class.Rogue,Stats(8,10,8,8,8,8))


   playerParty = []
   opposingParty = []

   playerParty.append(Needle)
   playerParty.append(Squee)

   opposingParty.append(GoblinRogue)
   opposingParty.append(GoblinLackey)
   opposingParty.append(GoblinBoss)
   opposingParty.append(GoblinAmbusher)

   GroupFight(playerParty,opposingParty)


if __name__ == "__main__":
    main()