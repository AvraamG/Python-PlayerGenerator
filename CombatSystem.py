from Character import Character

engagementISOver = False

#TODO split the allParticipants to 2 Parties instead. One for the players and 1 for the encounter party
def GroupFight(allParticipants:list[Character]):
    print("------- Encounter -------")
    for participant in allParticipants:
        print(f"{participant.Name} has engaged")

    while not engagementISOver:
        StartCombat(allParticipants)
        CheckIfCombatHasEnded()

def StartCombat(allParticipants:list[Character]):

   print(f"\n------- Rolling for Initiatives -------")
   sorterCharacters =  RollCharacterInitiatives(allParticipants)
   print(f"\n------- Combat -------")

   for i in range(len(sorterCharacters)):
       print(f"\n------- {sorterCharacters[i].Name}'s turn -------")
       attacker = sorterCharacters[i]
       target = sorterCharacters[(i + 1) % len(sorterCharacters)]
       attacker.Attack(target)

def RollCharacterInitiatives(allCharacters:list[Character]) ->list[Character]:
    initiativeResults = []
    for character in allCharacters:
        initiativeRoll = character.RollForInitiative()
        playerRoll = [character,initiativeRoll]
        initiativeResults.append(playerRoll)

    #TODO resolve ties
    sorted_results = sorted(initiativeResults, key=lambda x: x[1])
    return [name for name, _ in sorted_results]

def CheckIfCombatHasEnded():
    #TODO not sure yet but probably I should have 2 opposing parties in combat. The combat should be over if 1 entire party cant participate in combat *Run, Die, Surrender?
   global engagementISOver
   engagementISOver=True

