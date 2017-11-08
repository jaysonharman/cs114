print("GET READY FOR BATTLE!")
print("")
print("")
print("Press ENTER to continue")
input()
print("")

# give user 50 mp
# subtract 10 mp
# until mp are zero


mp = 50
hp = 50

while mp >= 0:
    print("User has", mp, "Magic points left")
    print("")
    print("Press ENTER to attack")
    print("")
    input()
    mp -= 5
    print("User has used 5 Magic points")


for hp in range(50):
    print("You have lost a total of", hp, "hit points.")
    print("")
    print("")
    print("The dragon attacks you...")
    print("")
    print("Press Enter to try and avoid being attacked.")
    input()
