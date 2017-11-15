import random


hp = 10
mp = 10

def health(HITPOINTS):
    while (mp > 0) == True:
        print("you have", mp, " magic points")
    mp -= random.randint(1,10)


def attack(DEATH):
    for attack in range(5):
        random_damage = random.randint(1,10)
    print(hp)
    print("You were attacked by a were-whale", random_damage, " damage.")
    hp -= random_damage
