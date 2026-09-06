import math
#function calculate_unit_price 2 parameter
#diameter of pizza (cm) & price in euros

#tell user which provide better value (smaller unit price)

#main program: ask user diameter + price of 2 pizzas

diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (euros): "))
diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (euros): "))

#function calculate, return unit price per square meter
def calculate_unit_price (diameter, price):
    diameter_m = diameter/100
    unit_price = price/(diameter_m **2/4*math.pi)
    return unit_price

unit_price1 = calculate_unit_price(diameter1,price1)
unit_price2 = calculate_unit_price(diameter2,price2)

print(f"Unit price of the first pizza: {unit_price1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unit_price2:.2f} euros/m²")

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")

