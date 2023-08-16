import random
import pdb

class Item:
    def __init__(self, name, item_type, description, prop, effect_type, base_effect, magnitude=0):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.prop = prop
        self.effect_type = effect_type
        self.base_effect = base_effect
        self.magnitude = magnitude

    def enact_effect(self, target):
        e_low = self.base_effect - self.magnitude
        e_high = self.base_effect + self.magnitude
        final_effect = random.randrange(e_low, e_high)
        print(f'EFFECT {final_effect}')
        target.take_damage(final_effect, self.effect_type)

