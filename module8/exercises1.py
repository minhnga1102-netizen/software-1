
#ask user number of a month
number_of_month = int(input("Enter the number of a month (1-12): "))

#a function takes number-month as parameter
def get_season (number_of_month):
    #save seasons as str into a tuple
    #define each season last 3 months, Dec as 1st month of winter
    seasons = {
        'winter':(12,1,2),
        'spring':(3,4,5),
        'summer':(6,7,8),
        'autumn':(9,10,11)
    }
    for season, months in seasons.items():
        if number_of_month in months:
            #print winter, spring, summer, autumn
            return season

#validate input
if number_of_month < 1 or number_of_month> 12:
    print(f"You entered: {number_of_month}\nPlease enter a number between 1 and 12.")
else:
    season = get_season(number_of_month)
    print(f"You entered: {number_of_month}\nThe season is {season}.")

# def get_season (number_of_month):
#     season = ''
#     if number_of_month in [12,1,2]:
#         season = 'winter'
#     elif number_of_month in [3,4,5]:
#         season = 'spring'
#     elif number_of_month in [6,7,8]:
#         season = 'summer'
#     elif number_of_month in [9,10,11]:
#         season = 'autumn'
#     return season

# # asks the user for a month number (1-12) 
# number_of_month = int(input("Enter the number of a month (1-12): "))

# # function takes a month number as parameter
# def get_season (number_of_month):
#     # Save the seasons as STR into a tuple. 
#     seasons = {
#         'winter':(12,1,2),
#         'spring':(3,4,5),
#         'summer':(6,7,8),
#         'autumn':(9,10,11)
#     }
#     #return season (tuple as return value)
#     for season, months in seasons.items():
#         if number_of_month in months:
#             return season
   

# season = get_season(number_of_month)

# # The program should validate that the user's input is a valid month number
# # The program should print which season the month belongs to

# if number_of_month < 1 or number_of_month > 12:
#     print(f"You entered: {number_of_month}\nPlease enter a number between 1 and 12.")
# else: 
#     print(f"You entered: {number_of_month}\nThe season is {season}.")


