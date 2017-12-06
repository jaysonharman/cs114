import random

print("PRESS ENTER TO ENTER THE DUNGEON")
input()

spam = ['WareWolf', 'Zombie', 'Evil Wizard','Dungeon Guard']

def battle(spam):
    randomenemy = random.randint(0,3)
    if randomenemy == 0:
        return print("A " + spam[0] + " has attacked you!" )
    elif randomenemy == 1:
        return print("A " + spam[1] + " has attacked you!" )
    elif randomenemy == 2:
        return print("A " + spam[2] + " has attacked you!" )
    elif randomenemy == 3:
        return print("A " + spam[3] + " has attacked you!" )

def health():
    mp = 50
    hp = 50

    while mp >= 0:
        print("User has", mp, "Magic points")
        print("")
        print("Press ENTER to attack")
        print("")
        input()
        mp -= 5
        



def main():
    battle(spam)
    health()

main()
