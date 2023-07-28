from classes.game import Person, bcolors
import pdb


def main():
    magic = [{'name' : 'Fire', 'cost' : 10, 'dmg' : 10},
             {'name' : 'Ice', 'cost' : 10, 'dmg' : 20},
             {'name' : 'Wind', 'cost' : 10, 'dmg' : 30},
             {'name' : 'Thunder', 'cost' : 10, 'dmg' : 40},
             {'name' : 'Cure', 'cost' : 20, 'dmg' : 40}]
    player = Person(460, 65, 60, 34, magic)
    enemy = Person(200, 65, 45, 25, magic)

    player.targets = [enemy]
    enemy.targets = [player]

    print(f'{bcolors.FAIL}{bcolors.BOLD}An Enemy Attacks!{bcolors.ENDC}')
    running = True
    target = enemy
    while running:
        print('=' * 72)
        choice = player.choose_action()
        print(f'Player chooses {choice["name"]}\n')
        choice['function']()

        echoice = enemy.choose_action(1)
        print(f'Entity chooses {echoice["name"]}\n')

        if enemy.hp < 1:
            print(f'{bcolors.OKGREEN}{enemy.name} has been defeated!{bcolors.ENDC}')
            running = False
        if player.hp < 1:
            print(f'{bcolors.FAIL}{player.name} has been defeated!{bcolors.ENDC}')
            running = False

    print("Thanks for playing!")


if __name__ == '__main__':
    main()
