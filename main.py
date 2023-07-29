from classes.game import Person, bcolors
import pdb
from classes.magic import Spell

def main():
    player_magic = [Spell('Fire', 10, 100, 'harm'),
             Spell('Ice', 20, 200, 'harm'),
             Spell('Wind', 30, 300, 'harm'),
             Spell('Thunder', 15, 150, 'harm'),
             Spell('Cure', 40, 50, 'heal')]

    player = Person(460, 15, 60, 34, player_magic, name = 'Player')
    party = [player]
    enemy1 = Person(200, 65, 45, 25, player_magic, name = 'Enemy 1')
    enemy2 = Person(18, 65, 45, 25, player_magic, name = 'Enemy 2')
    enemies = [enemy1, enemy2]
    player.targets = enemies

    print(f'{bcolors.FAIL}{bcolors.BOLD}An Enemy Attacks!{bcolors.ENDC}')
    running = True
    while running:
        print(f'{"=" * 72}')
        print('Player\'s Turn')
        choice = player.choose_action()
        print(f'Player chooses {choice["name"]}\n')
        choice['function']()
        print(f'{"=" * 72}')

        for enemy in enemies:
            enemy.current_target = player
            if enemy.hp < 1:
                print(f'{bcolors.OKGREEN}{enemy.name} has been defeated!{bcolors.ENDC}')
                enemies.remove(enemy)
            enemy.targets = [player]
            print(f'{enemy.name}\'s Turn')
            echoice = enemy.choose_action(1, player)
            print(f'{enemy.name} chooses {echoice["name"]}\n')
            echoice['function'](enemy.current_target)
            print(f'{"=" * 72}')

            if player.hp < 1:
                print(f'{bcolors.FAIL}{player.name} has been defeated!{bcolors.ENDC}')
                running = False

        if len(enemies) < 1:
            running = False
            print('You win!')

    print("Thanks for playing!")


if __name__ == '__main__':
    main()
