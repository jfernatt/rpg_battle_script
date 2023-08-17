from classes.game import Person, bcolors
from classes.magic import Spell
from classes.items import Item


fire_spell = Spell('Fire', 10, 100, 'harm')
ice_spell = Spell('Ice', 20, 200, 'harm')
wind_spell = Spell('Wind', 30, 300, 'harm')
thunder_spell = Spell('Thunder', 15, 150, 'harm')
cure_spell = Spell('Cure', 40, 50, 'heal')

potion = Item("Healing Potion", "potion", "A healing tincture in a small glass bottle. The taste is rather bitter. Heals for 40HP", "PLACEHOLDER", 'heal', 20, 5)
grenade = Item("Grenade", "throwable", "Small hand grenade. Deals x damage", "PLACEHOLDER", 'physical', 40, 10)


def make_status_bar(party, enemies):
    for player in party:
        player.create_status_bar()
    for enemy in enemies:
        enemy.create_status_bar()


def check_end_conditions(party, enemies):
    game_over = True
    for player in party:
        if player.hp > 0:
            game_over = False
    player_win = True
    for enemy in enemies:
        if enemy.hp > 0:
            player_win = False
    if game_over:
        print(f'{bcolors.FAIL}Your party has been defeated!{bcolors.ENDC}')
        quit()
    elif player_win:
        print('You win!')
        return False
    return True


def main():
    player_magic = [fire_spell,
                    ice_spell,
                    wind_spell,
                    thunder_spell,
                    cure_spell]

    player_inventory = [{'item' : potion, 'qty' : 5},
                        {'item' : grenade, 'qty' : 5}]

    player1 = Person(460, 45, 60, 34, player_magic, player_inventory, name='Doofy')
    player2 = Person(200, 80, 15, 14, player_magic, player_inventory, name="Floofy")
    party = [player1, player2]
    player_targets = [i for i in party]
    enemy1 = Person(200, 65, 45, 25, player_magic, name='Enemy 1')
    enemy2 = Person(18, 65, 45, 25, player_magic, name='Enemy 2')
    enemies = [enemy1, enemy2]
    player_targets.extend(enemies)
    print(f'{bcolors.FAIL}{bcolors.BOLD}An Enemy Attacks!{bcolors.ENDC}')

    for player in party:
        player.targets = player_targets

    running = True
    while running:
        print(f"NAME{' ' * 40}HP{' ' * 40}MP")
        for player in party:
            make_status_bar(party, enemies)
            print(f'{"=" * 72}')
            print(f'{player.name}\'s Turn')
            choice = player.choose_action()
            print(f'Player chooses {choice["name"]}\n')
            choice['function']()
            print(f'{"=" * 72}')
            for enemy in enemies:
                if enemy.hp < 1:
                    print(f'{bcolors.OKGREEN}{enemy.name} has been defeated!{bcolors.ENDC}')
                    enemies.remove(enemy)
                    running = check_end_conditions(party, enemies)
        for enemy in enemies:
            enemy.current_target = party[0]
            enemy.targets = party
            print(f'{enemy.name}\'s Turn')
            echoice = enemy.choose_action(1, enemy.current_target)
            print(f'{enemy.name} chooses {echoice["name"]}\n')
            echoice['function'](enemy.current_target)
            print(f'{"=" * 72}')

            if enemy.current_target.hp < 1:
                print(f'{bcolors.FAIL}{enemy.current_target.name} has been defeated!{bcolors.ENDC}')
                running = False
                for target in enemy.targets:
                    if target.hp < 1:
                        running = check_end_conditions(party, enemies)
        if not running:
            print(f'{bcolors.OKGREEN}Your party has defeated the enemies!{bcolors.ENDC}')
    print("Thanks for playing!")


if __name__ == '__main__':
    main()
