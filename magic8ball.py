import random

print("MAGIC 8 BALL: THE COMPUTER")
input()
print("Type in your name to reveal your fortune, then push enter")
input()

random_num = random.randint(1, 9)

print("Your fortune = ")

if random_num == 1:
    print("You will never die.")
if random_num == 2:
    print("You will die tomorrow.")
if random_num == 3:
    print ("You will die very old..")
if random_num == 4:
    print("You will die happy.")
if random_num == 5:
    print("You will die alone.")
if random_num == 6:
    print ("You will die young.")
if random_num == 7:
    print("You will die broke.")
if random_num == 8:
    print("You will die hated by the world.")
if random_num == 9:
    print ("You will die loved by the whole world.")
