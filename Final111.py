import random
import time


def health():
    php = 500
    ehp = 100

    while php >= 0:
        print("User has", php, "Health points left")
        print("")
        print("Enemy has", ehp, "Health points left")
        print("Press ENTER to attack")
        print("")
        input()
        randomhealth = random.randint(0,2)

        if randomhealth == 0:
          return print("You've been hit!")
          php -= 20

        elif randomhealth == 1:
          return print("You hit the enemy!")
          ehp -= 10

        elif randomhealth == 2:
          return print("Critial Hit!")
          ehp -= 20

    while ehp <= 0:
        print("You've defeated your enemy!")

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
    health()






print("PRESS ENTER TO ENTER THE DUNGEON")
input()

def intro():
    print("Welcome to the mysterious dungeon...")
    time.sleep(2)
    print("")
    print("Which way will you choose to go?")
    time.sleep(2)

def path():
    pathchoice = ""

    pathchoice = input("Left or Right?")

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
      print("This path is empty, keep going...PRESS ENTER")
      input()
      path()
      encounter()
      print("")

    elif randomencounter == 2:
      print("This path is empty, keep going...PRESS ENTER")
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
    print("")
    path()
    print("")
    encounter()
    print("")



main()
