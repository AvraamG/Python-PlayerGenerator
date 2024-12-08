from Character import Character

engagementISOver = False


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

#I should probably work with lists here but for now just have 2 characters duel.
def RollCharacterInitiatives(allCharacters:list[Character]) ->list[Character]:
    #I ll use a list of Tuples
    initiativeResults = []
    for character in allCharacters:
        initiativeRoll = character.RollForInitiative()
        playerRoll = [character,initiativeRoll]
        initiativeResults.append(playerRoll)

    #I should check and resolve ties
    #There is something wrong here
    sorted_results = sorted(initiativeResults, key=lambda x: x[1])
    return [name for name, _ in initiativeResults]

def CheckIfCombatHasEnded():
   global engagementISOver
   engagementISOver=True

