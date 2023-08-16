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
    def __init__(self, hp, mp, atk, df, magic, inventory=[], targets=None, name='Entity'):
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
                        {'name' : 'Use Item', 'function' : self.choose_item},
                        {'name' : 'Run Away!', 'function' : self.flee}]
        self.inventory = inventory

    def generate_damage(self, target=None, type='physical'):
        if not target:
            self.change_target()
        damage = random.randrange(self.atkl, self.atkh)
        self.current_target.take_damage(damage, type)

    def cast_spell(self, spell):
        self.change_target()
        if self.mp >= spell.cost:
            spell.generate_spell_damage(self.current_target)
            self.mp -= spell.cost
        else:
            print(f'{bcolors.FAIL}Not enough magic points!{bcolors.ENDC}')
            self.choose_action()

    def use_item(self, item):
        self.change_target()
        item.enact_effect(self.current_target)
        #REDUCE INVENTORY BY 1

    def restore_health(self, spell):
        mgl = spell['dmg'] - 5
        mgh = spell['dmg'] + 5
        convalescence = random.randrange(mgl, mgh)
        if self.hp + convalescence > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += convalescence

    def take_damage(self, dmg, type):
        if type in ['harm', 'physical']:
            print(f'{bcolors.FAIL}{self.name} takes {dmg} points of {type} damage...{bcolors.ENDC}')
            self.hp -= dmg
        elif type == 'heal':
            print(f'{bcolors.OKBLUE}{self.name} heals {dmg} points{bcolors.ENDC}')
            self.hp += dmg
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
            print(f"{self.name}{' ' * 20}{self.hp}/{self.max_hp}{' ' * 20}{self.mp}/{self.max_mp}")
            print(f'  HP:{self.hp}/{self.max_hp}\n  MP:{self.mp}/{self.max_mp}')
            [print(f'{i}. {k["name"]}') for i, k in options.items()]
            try:
                selection = int(input("Choose an action: "))
            except Exception as e:
                # log e
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
                self.current_target = options[selection]['object']
            except Exception as e:
                # log e
                print('Invalid Selection, please try again...\n')
                self.change_target()
        else:
            print('No other targets available')

    def flee(self):
        flee = random.randint(0, 1)
        if flee:
            # Stop Combat
            quit()
        else:
            print(f'{bcolors.FAIL}{bcolors.BOLD}You were unable to flee from combat{bcolors.ENDC}')

    def choose_magic(self):
        options = {}
        [options.update({i+1 : {'name' : k.name, 'cost' : k.cost, 'dmg' : k.dmg, 'object' : k}}) for i, k in enumerate(self.magic)]
        print(f'Current MP: {self.mp}')
        [print(f'{i}. {k["name"]}, MP: {k["cost"]}') for i, k in options.items()]
        try:
            selection = int(input("Choose a spell: "))
            self.cast_spell(options[selection]['object'])
        except Exception as e:
            # log e
            print('Invalid Selection, please try again...\n')
            self.choose_magic()

    def choose_item(self):
        options = {}
        [options.update({i+1 : {'name' : k['item'].name, 'description' : k['item'].description, 'qty' : k['qty'], 'object' : k['item']}}) for i, k in enumerate(self.inventory) if k['qty'] > 0]
        [print(f'{i}. {k["name"]}, Qty: {k["qty"]}\n  Description: {k["description"]}, ') for i, k in options.items()]
        try:
            selection = int(input("Choose an item to use: "))
            self.use_item(options[selection]['object'])
            reduce_inv = [i for i in self.inventory if options[selection]['object'] is i['item']]
            reduce_inv[0]['qty'] -= 1
        except Exception as e:
            # log e
            pdb.set_trace()
            print('Invalid Selection, please try again...\n')
            self.choose_item()