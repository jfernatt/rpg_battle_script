import random

class Enemy():
    hp = 200
    def __init__(self, hp, mp, atkl=60, atkh=90):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atkl
        self.atkh = atkh

    def get_hp(self):
        return self.hp

    def get_atk(self):
        return random.randrange(self.atkl,self.atkh)