weight = int(input("Enter the weight of the package in kilograms from 1-20."))
while weight < 1 or weight > 20:
    weight = int(input("Invalid weight. Please enter the package weight from 1-20"))

miles = int(input("Enter the shipping distance in miles from 10-3000."))
while miles < 10 or miles > 3000:
    miles = int(input("Invalid input. Please enter the shipping distance from 10-3000."))

if weight <= 2:
    cost = (miles / 500) * 1.1
    rate = 1.1
elif weight <= 6:
    cost = (miles / 500) * 2.2
    rate = 2.2
elif weight <= 10:
    cost = (miles / 500) * 3.7
    rate = 3.7
else:
    cost = (miles / 500) * 4.8
    rate = 4.8

print("Package weight: ", weight, "kg")
print("Shipping Distance: ", miles, "miles")
print("Shipping rate per 500 miles: $", rate)
print("Total shipping charge: $", cost)