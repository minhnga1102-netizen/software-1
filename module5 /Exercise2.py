length_inches = float(input ("Enter length in inches (negative value to quit): "))

while length_inches >= 0:
    length_cm = length_inches*2.54
    
    print (f"{length_inches} inches is {length_cm:.2f} centimeters")
    length_inches = float(input ("Enter length in inches (negative value to quit): "))

print("Program ended.")

