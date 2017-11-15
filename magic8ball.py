
import random
"""
random number function
"""

def getNumber(randomnumber):

    if randomnumber == 1:
        return "Your future does not look good"
    elif randomnumber == 2:
        return "Your future looks bright"
    elif randomnumber == 3:
        return "Your future is filled with bad news"
    elif randomnumber == 4:
        return "Your future is filled with happiness"
    elif randomnumber == 5:
        return "Your future will end soon"
    elif randomnumber == 6:
        return "Your future will last a very long time"
    elif randomnumber == 7:
        return "Your future is scary"
    elif randomnumber == 8:
        return "Your future is happy"
    elif randomnumber == 9:
        return "Your future is death"

r = random.randint(1,9)
magic_ball = getNumber(r)

print(magic_ball)
