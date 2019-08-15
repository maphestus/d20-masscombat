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

    # DO I NEED THIS???
    # def __init__(self, armyattack, armydefense):
    #    self.armyattack = armyattack
    #    self.armydefense = armydefense

    def battle(self, armyattack, armydefense):
        rounds = 0
        while armyattack.hp > 0 and armydefense.hp > 0:
            # Offense Check of both armies
            armya = sum(dice.roll('1d20')) + armyattack.om
            armyb = sum(dice.roll('1d20')) + armydefense.om
            print(f'{armyattack.name} rolled {armya}')
            print(f'{armydefense.name} rolled {armyb}')

            # Defense Check of both armies
            armyadmg = armyb - armyattack.dv
            if armyadmg > 0:
                armyattack.hp = armyattack.hp - armyadmg
            armybdmg = armya - armydefense.dv
            if armybdmg > 0:
                armydefense.hp = armydefense.hp - armybdmg
            print(f'{armyattack.name} did {armybdmg} to {armydefense.name}, hp now {armydefense.hp}')
            print(f'{armydefense.name} did {armyadmg} to {armyattack.name}, hp now {armyattack.hp}')

            # Morale Check
            if armyattack.hp <= armyattack.acr:
                routa = sum(dice.roll('1d20')) + armyattack.morale
                if routa < 15:
                    armyattack.hp = 0
                    print(f'{armyattack.name} routed!')
            if armydefense.hp <= armydefense.acr:
                routb = sum(dice.roll('1d20')) + armydefense.morale
                if routb < 15:
                    armydefense.hp = 0
                    print(f'{armydefense.name} routed!')

            rounds = rounds + 1


OrcArmy = Army("Orcs", 100, "orc", 11, 13, 2, 2, 0)
HumArmy = Army("Humans", 100, "human", 16, 13, 3, 3, 0)

# print(OrcArmy.__dict__)
# print(HumArmy.__dict__)

battle1 = Combat()

battle1.battle(OrcArmy, HumArmy)

die = dice.roll('1d20')
score = sum(die) + OrcArmy.om
# print(f'Rolled {die}, total is {score}')
