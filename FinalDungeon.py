import random
import time

def outro():
    print("You have killed the dungeon master!")
    time.sleep(2)
    print("The people in town are very thankful")
    time.sleep(2)
    print("THE END")

def attack(php, ehp):
    randomattack = random.randint(0,2)

    if randomattack == 0:
        php -= 20
        print("You've been hit!")

    elif randomattack == 1:
        ehp -= 10
        print("You hit the enemy!")

    elif randomattack == 2:
        ehp -= 20
        print("Critial Hit!")

def health():
    php = 500
    ehp = 100

    while ehp >= 0:
        print("Your enemy has ", ehp, "health points left")
        time.sleep(1)
        print("You have ", php, "health points left")
        time.sleep(1)
        print("Press ENTER to attack")
        input()
        attack(php, ehp)
        time.sleep(1)

    while ehp <= 0:
        print("You have killed the Dungeon Master ")
        outro()


spam = ['WareWolf', 'Zombie', 'Evil Wizard','Dungeon Guard']

def battle(spam):

    randomenemy = random.randint(0,3)
    if randomenemy == 0:
        return print("A " + spam[0] + " has attacked you!" )
        time.sleep(1)

    elif randomenemy == 1:
        return print("A " + spam[1] + " has attacked you!" )
        time.sleep(1)

    elif randomenemy == 2:
        return print("A " + spam[2] + " has attacked you!" )
        time.sleep(1)

    elif randomenemy == 3:
        return print("A " + spam[3] + " has attacked you!" )
        time.sleep(1)



print("PRESS ENTER TO ENTER THE DUNGEON")
input()

def intro():
    print("Welcome to the mysterious dungeon...")
    time.sleep(2)
    print("")
    print("Which way will you choose to go?")
    time.sleep(1)

def path():
    pathchoice = ""

    pathchoice = input("Left or Right? "
    )

    print("")

    if pathchoice == "left":
        print("You've choosen left")
    elif pathchoice == "right":
        print("You've choosen right")

def encounter():
    randomencounter = random.randint(0,3)

    if randomencounter == 0:
      print("This path is empty, keep going...PRESS ENTER")
      input()
      path()
      encounter()
      print("")

    elif randomencounter == 1:
      print("It's quiet...a little too quiet...Keep going...PRESS ENTER")
      input()
      path()
      encounter()
      print("")

    elif randomencounter == 2:
      print("Find a different path, this one is empty...PRESS ENTER")
      input()
      path()
      encounter()
      print("")

    elif randomencounter == 3:
      print("Something is coming...")
      time.sleep(2)
      print("Prepare to Fight!")
      print("")
      time.sleep(2)
      battle(spam)


def main():
    intro()
    path()
    encounter()
    health()

main()
