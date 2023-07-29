import random
import pdb

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic, targets=None, name='Entity'):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.targets = targets
        self.current_target = None
        self.actions = [{'name' : 'Attack', 'function' : self.generate_damage},
                        {'name' : 'Magic', 'function' : self.choose_magic},
                        {'name' : 'Run Away!', 'function' : self.flee}]

    def generate_damage(self):
        self.change_target()
        damage = random.randrange(self.atkl, self.atkh)
        self.current_target.take_damage(damage)

    def cast_spell(self, spell):
        self.change_target()
        if self.mp >= spell['cost']:
            spell.generate_spell_damage(spell, self.current_target)
            self.mp -= spell['cost']
        else:
            print(f'{bcolors.FAIL}Not enough magic points!{bcolors.ENDC}')
            self.choose_action()

    def restore_health(self, spell):
        mgl = spell['dmg'] - 5
        mgh = spell['dmg'] + 5
        convalescence = random.randrange(mgl, mgh)
        if self.hp + convalescence > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += convalescence

    def take_damage(self, dmg):
        print(f'{self.name} takes {dmg} points of damage...')
        self.hp -= dmg
        if self.hp < 1:
            self.hp = 0
        return self.hp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self, selection=None, target=None):
        options = {}
        [options.update({i+1 : {'name' : k['name'], 'function' : k['function']}}) for i, k in enumerate(self.actions)]
        if selection:
            try:
                return options[selection]
            except Exception as e:
                print(e)
                quit()
        else:
            [print(f'{i}. {k["name"]}') for i, k in options.items()]
            try:
                selection = int(input("Choose an action: "))
            except Exception as e:
                #log e
                print('Invalid Selection, please try again...\n')
                self.choose_action(target)
            else:
                return options[selection]

    def change_target(self, target=None):
        if target:
            self.current_target = target
            return
        if len(self.targets) >= 1:
            options = {}
            try:
                [options.update({i + 1: {'name': k.name, 'hp' : k.hp, 'object' : k}}) for i, k in enumerate(self.targets)]
            except Exception as e:
                print(e)
                print('Error enumerating targets')
                pdb.set_trace()
            [print(f'{i}. {k["name"]} - HP: {k["hp"]}') for i, k in options.items()]
            try:
                selection = int(input("Choose a target: "))
            except Exception as e:
                # log e
                print('Invalid Selection, please try again...\n')
            else:
                self.current_target = options[selection]['object']
        else:
            print('No other targets available')

    def flee(self):
        flee = random.randint(0, 1)
        if flee:
            #Stop Combat
            quit()
        else:
            print(f'{bcolors.FAIL}{bcolors.BOLD}You were unable to flee from combat{bcolors.ENDC}')

    def choose_magic(self):
        options = {}
        [options.update({i+1 : {'name' : k.name, 'cost' : k.cost, 'dmg' : k.dmg}}) for i, k in enumerate(self.magic)]
        print(f'Current MP: {self.mp}')
        [print(f'{i}. {k["name"]}, MP: {k["cost"]}') for i, k in options.items()]
        try:
            selection = int(input("Choose a spell: "))
        except Exception as e:
            # log e
            print('Invalid Selection, please try again...\n')
            self.choose_magic()
        else:
            self.cast_spell(options[selection])
