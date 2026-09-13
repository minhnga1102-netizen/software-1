#store KEY-VALUE pairs
numbers = {
    "Juha":"123",
    "adam":"456",
    "mia":"789"
}

print(numbers)

print (numbers["adam"])

if "adam" in numbers:
    print("lowercase adam found")
    print(numbers["adam"])

# print(numbers[0])

for item in numbers:
    print(item)

#if need the values, use value method
if "Juha" in numbers:
    print("Juha found")
