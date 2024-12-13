#TODO I should use min max so a stat can be min 1 and max 30.
from __future__ import annotations
class Stats:
    Strength:int
    Dexterity:int
    Constitution:int
    Intelligence:int
    Wisdom:int
    Charisma:int

    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.Strength = strength
        self.Dexterity = dexterity
        self.Constitution = constitution
        self.Intelligence = intelligence
        self.Wisdom = wisdom
        self.Charisma = charisma
    @classmethod
    def GenerateStatsAllTen(cls) -> Stats:
        return cls (10,10,10,10,10,10)

#This is how you enable += operations
    def __iadd__(self, other):
        if not isinstance(other, Stats):
            return NotImplemented
        self.Strength += other.Strength
        self.Dexterity += other.Dexterity
        self.Constitution += other.Constitution
        self.Intelligence += other.Intelligence
        self.Wisdom += other.Wisdom
        self.Charisma += other.Charisma
        return self
