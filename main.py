import CombatSystem
from Player import Player
from NPC import  NPC
from Stats import Stats
from GameMechanics import Class,Race
from CombatSystem import GroupFight

def main():
   Needle = Player("Needle",3,Race.Halfling,Class.Bard,Stats(10,10,10,10,10,10))
   #Squee = NPC("Squee",1,Race.HalfDrow,Class.Rogue,Stats(10,10,10,10,10,10))
   Goblin1 = NPC("Goblin NPC",1,Race.Goblin,Class.Rogue,Stats(10,10,10,10,10,10))
   duelCharacters = [Goblin1,Needle]
   GroupFight(duelCharacters)
   #TODO create a GameMechanic Duel method that takes 2 Characters and displays the combat in turns until someone dies
   #Squee.Attack(Needle)
   #Needle.Attack(Squee)


if __name__ == "__main__":
    main()