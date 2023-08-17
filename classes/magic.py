import random


class Spell:
    def __init__(self, name, cost, dmg, dmg_type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.dmg_type = dmg_type

    def generate_spell_damage(self, current_target):
        mgl = self.dmg - 5
        mgh = self.dmg + 5
        damage = random.randrange(mgl, mgh)
        current_target.take_damage(damage, dmg_type=self.dmg_type)
