import random

print("PRESS ENTER TO ENTER THE DUNGEON")
input()

spam = ['Guard', 'Monster', 'WareWolf', 'Wizard']

def intro():
    print("You have entered the dungeon...")
    print("Would you like to go left or right?")
    input()


def battle(spam):
    randomenemy = random.randint(0,3)
    if randomenemy == 0:
        return print ("You have been challenged by " + spam[0] + ", prepare to die!")
    elif randomenemy == 1:
        return print ("A " + spam[2] + " has came out of nowhere and attacked you!")
    elif randomenemy == 2:
        return print ("A drunken old " + spam[3] + " has attacked you!")
    elif randomenemy == 3:
        return print ("You have awoken the " + spam[1] + " prepare to fight til the death!")

    # r = random.randint(1,5)
    # battle_enemy = battle(r)


def main():
    battle(spam)

main()
