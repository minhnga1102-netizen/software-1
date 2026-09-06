
#main program: ask for a volume in GALLONS
gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

#function return number converted to L
def gallons_to_liters (gallons):
     liters = gallons * 3.785
     return liters

#until negative gallons value
while gallons >=0: 
     liters = gallons_to_liters(gallons)
     print(f"{gallons} American gallons is {liters:.2f} liters.")
     gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
else:
    print("Program finished.")