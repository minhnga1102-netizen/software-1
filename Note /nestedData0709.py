#combine list & dictionary 
# each list contains numbers of dictionary, inside key:value

cars = [
    {
        "brand":"toyota",
        "model": "corolla",
        "year":"2018"
    },
    {
        "brand":"ford",
        "model": "focus",
        "year":"2019"
    },
    {
        "brand":"vw",
        "model": "id",
        "year":"2020"
    }
]

#retrieve key:value
second_car = cars[1]
print(second_car)

first_car_brand = cars[0]["brand"]
print(f"The brand of the first car is {first_car_brand}")

#iterate to print each car's info
#wrote cars['brand] and error: CARS is list - only indices by integer/slice  not str
#ex: cars[0], cars[0:2] not cars['brand']
#CAR is dictionary - car['brand'], key as STR OK

for car in cars:
    print(f"Brand: {car["brand"]}, Model: {car["model"]}, Year: {car["year"]}")