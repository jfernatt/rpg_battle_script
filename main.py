from classes.game import Person, bcolors


def main():
    magic = [{'name' : 'Fire', 'cost' : 10, 'dmg' : 10},
             {'name' : 'Ice', 'cost' : 10, 'dmg' : 20},
             {'name' : 'Wind', 'cost' : 10, 'dmg' : 30},
             {'name' : 'Thunder', 'cost' : 10, 'dmg' : 40},]
    player = Person(460, 65, 60, 34, magic)


if __name__ == '__main__':
    main()
