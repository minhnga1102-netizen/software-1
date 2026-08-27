year = int(input("Enter a year: "))

#special rule always come first %400==0 leap
if year % 400 ==0: 
    print(f"{year} is a leap year.")

#if not %400==0,even %100==0 not a leap year 
elif year % 100 == 0:
    print(f"{year} is not a leap year.")

#basic rules come last, after ruling out above rules
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")