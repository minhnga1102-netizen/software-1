print("\nAirport Data Management")
print("1. Enter a new airport")
print("2. Fetch airport information")
print("3. Quit")

airports = {}
user_input = input("Please choose an option (1-3): ")

while user_input != "3":
    if user_input == "1":
        code= input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")
    #dictionary, key-value assignment, KEY=CODE, VALUE=NAME
        airports[code]=name
        print(f"Airport {name} with ICAO code {code} has been added.")
    elif user_input == "2":
        code = input("Enter the ICAO code: ")
        #airport[code] = name!!! 
        if code in airports:
            print(f"The airport with ICAO code {code} is {airports[code]}.")
        else:
            print(f"No airport found with ICAO code {code}.")
    print("\nAirport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    user_input = input("Please choose an option (1-3): ")

print("Thank you for using the Airport Data Management system. Goodbye!")
    
    