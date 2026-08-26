talents = float(input ("Enter talents: "))
pounds = float(input ("Enter pounds: "))
lots = float(input ("Enter lots: "))

total_grams = talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3
kilograms = int(total_grams/1000)
remaining_grams = float (total_grams - kilograms*1000)

#print ("The weight in modern units:", kilograms, "kilograms and", remaining_grams, "grams.")
print ("The weight in modern units:")
print (f"{kilograms} and {remaining_grams:.2f}")
#print (f"The weight in modern units:\n{kilograms} kilograms and {remaining_grams:.2f} grams.")