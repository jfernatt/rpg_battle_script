from classes.enemy import Enemy


enemy1 = Enemy(30, 40)
print(enemy1.get_atk())
enemy2 = Enemy(90, 150)
print(enemy2.get_atk())

'''
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp -= dmg
    if playerhp < 31:
        playerhp = 30
    print(f'Enemy attacks for {dmg} points of damage... Current HP is {playerhp}')

    if playerhp > 30:
        continue

    print('You have passed out and wake up at the nearest Inn')
    break
'''