
print ("Please type number from 1-99")
num = int(input())

tens = num // 10
ones = num % 10


if tens == 2:
    tens_word = "Twenty"
elif tens == 3:
    tens_word = "Thirty"
elif tens == 4:
    tens_word = "Fourty"
elif tens == 5:
    tens_word = "Fifty"
elif tens == 6:
    tens_word = "Sixty"
elif tens == 7:
    tens_word = "Seventy"
elif tens == 8:
    tens_word = "Eighty"
elif tens == 9:
    tens_word = "Ninety"

if ones == 1:
    ones_word = "One"
elif ones == 2:
    ones_word = "Two"
elif ones == 3:
    ones_word = "Three"
elif ones == 4:
    ones_word = "Four"
elif ones == 5:
    ones_word = "Five"
elif ones == 6:
    ones_word = "Six"
elif ones == 7:
    ones_word = "Seven"
elif ones == 8:
    ones_word = "Eight"
elif ones == 9:
    ones_word = "Nine"

if tens == 0:
    output = ones_word
elif tens == 1:
    if ones == 1:
        output = "Eleven"
    elif ones == 2:
        output = "Twelve"
    elif ones == 3:
        output = "Thirteen"
    elif ones == 5:
        output = "Fifteen"
    else: output = ones_word + 'teen'

else:
    output = tens_word + '-' + ones_word

print(output)
