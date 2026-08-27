#Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
#a 4-digit code where each number is between 1 and 6.


import random

# test count = 0 and count = 1 OK
code = ''
count = 1
while count <= 3:
    digit = random.randint(0,9)
    code = code + str (digit)
    count +=1
print(f'3-digit code: {code}')


code = ''
count = 0
while count < 4:
    digit = random.randint(1,6) 
    code = code + str (digit)
    count +=1
print(f"4-digit code: {code}")