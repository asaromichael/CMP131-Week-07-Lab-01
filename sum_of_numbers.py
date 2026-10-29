value = int(input("Please enter a value over 1."))

while value < 1:
    value =int(input("Invalid input. Please enter a value over 1."))

total = 0
value += 1

for num in range(1, value):
    total += num

print("The sum of all integer leading up to your chosen integer is: ", total)