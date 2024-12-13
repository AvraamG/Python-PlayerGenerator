import CombatSystem
from Player import Player
from NPC import  NPC
from Stats import Stats
from GameMechanics import Class,Race
from CombatSystem import GroupFight

def main():
   Squee = Player("Squee",2,Race.Goblin,Class.Rogue,Stats(10,10,10,10,10,10))
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