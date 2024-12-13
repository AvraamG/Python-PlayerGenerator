import NPC
import Player
from Character import Character

combatHasEnded = False
allParticipants=[]
players = []
enemies = []


def GroupFight(playerParty:list[Character],opposingParty:list[Character]):
    global players
    global enemies
    global allParticipants
    turnIndex = 0

    players = playerParty
    enemies = opposingParty
    allParticipants = enemies + players

    allParticipants = RollCharacterInitiatives(allParticipants)
    print(f"Initiative order \n")
    for participant in allParticipants:
        print(f"{participant.Name}: {participant.Initiative}")


    while not combatHasEnded:
        #I have a bug here. If a player dies, it gets removed from the list. So the For loop might go out of bounds.
        if turnIndex >= len(allParticipants):  # Loop back to the start
            turnIndex = 0
        currentCharacter = allParticipants[turnIndex]

        if not combatHasEnded:
            print(f"\n------- {currentCharacter.Name}'s turn -------")
            attacker = currentCharacter
            target = attacker.PickTarget(allParticipants)
            attacker.Attack(target)
            # If the current character is still alive, move to the next one
            if currentCharacter in allParticipants:
                turnIndex += 1

    print(f"\n------- Combat has ended -------")

def RollCharacterInitiatives(allCharacters: list[Character]) -> list[Character]:
    initiativeResults = []
    for character in allCharacters:
        initiativeRoll = character.RollForInitiative()
        playerRoll = [character, initiativeRoll]
        initiativeResults.append(playerRoll)

    # Sort by initial rolls (descending)
    sorted_results = sorted(initiativeResults, key=lambda x: x[1], reverse=True)

    # Resolve ties
    i = 0
    while i < len(sorted_results):
        # Find all characters with the same roll
        tie_group = [sorted_results[i]]
        current_initiative = sorted_results[i][1]
        j = i + 1

        while j < len(sorted_results) and sorted_results[j][1] == current_initiative:
            tie_group.append(sorted_results[j])
            j += 1

        # If there's a tie, reroll within the group
        if len(tie_group) > 1:
            reroll_results = []
            for character, _ in tie_group:
                reroll = character.RollForInitiative()  # Reroll for tiebreaking
                reroll_results.append((character, reroll))

            # Sort by reroll (descending) to resolve the tie
            tie_group_sorted = sorted(reroll_results, key=lambda x: x[1], reverse=True)

            # Replace the tied group with the resolved order
            sorted_results[i:j] = tie_group_sorted

        # Move to the next group
        i = j

    # Return only the characters in the resolved order
    return [character for character, _ in sorted_results]





def RemoveCharacterFromCombat(deadCharacter:Character):
    global allParticipants
    if deadCharacter in allParticipants:
        allParticipants.remove(deadCharacter)
    else:
        print(f"Cant find {deadCharacter} in all participants")

    CheckIfCombatHasEnded()


def CheckIfCombatHasEnded():
   global combatHasEnded
   global allParticipants
   global players
   global enemies
   enemies = [character for character in allParticipants if character.IsEnemyToParty]
   players = [character for character in allParticipants if not character.IsEnemyToParty]

   print(f"Players remaining {len(players)}")
   print(f"Enemies remaining {len(enemies)}")

   if not enemies:
       print(f" ----- Party has won -----")
   if not players:
       print(f" ----- Enemies have won -----")

   combatHasEnded = not enemies or not players

#Dead enemies are not removed