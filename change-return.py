print('how much change to convert, less than 100?')
num_convert = int(input())
num_fivedollars = num_convert // 500
num_convert = num_convert - (num_fivedollars * 500)
num_dollars = num_convert // 100
num_convert = num_convert - (num_dollars * 100)
num_quarters = num_convert // 25
num_convert = num_convert - (num_quarters * 25)
num_dimes = num_convert // 10
num_convert = num_convert - (num_dimes * 10)
num_nickles = num_convert // 5
num_convert = num_convert - (num_nickles * 5)
num_pennies = num_convert // 1
num_convert = num_convert - (num_pennies * 1)
print("$5.00:", num_fivedollars)
print("$1.00:", num_dollars)
print("¢0.25:", num_quarters)
print("¢0.10:", num_dimes)
print("¢0.05:", num_nickles)
print("¢0.01:", num_pennies)
print("Running total", num_convert)
