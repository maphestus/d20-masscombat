import dice


class Army:

    def __init__(self, name, size, type, hp, dv, om, acr, morale):
        self.name = name
        self.size = size
        self.type = type
        self.hp = hp
        self.dv = dv
        self.om = om
        self.acr = acr
        self.morale = morale


class Combat:

    def __init__(self, armyattack, armydefense):
        self.armyattack = armyattack
        self.armydefense = armydefense

    def battle(self, armyattack, armydefense):
        rounds = 0


OrcArmy = Army("Orcs", 100, "orcs", 11, 13, 2, 2, 0)
HumArmy = Army("Human", 100, "human", 16, 13, 3, 3, 0)

# print(OrcArmy.__dict__)
# print(HumArmy.__dict__)
die = dice.roll('1d20')
score = sum(die) + OrcArmy.om
print(f'Rolled {die}, total is {score}')
