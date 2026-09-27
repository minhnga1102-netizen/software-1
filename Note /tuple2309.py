
tuple1=(2,4,6,8,10)

print(tuple1[4])
print(tuple1[2:5])

tuple2= (1,2,3)
(first, second, third) = tuple2
print(first)
one, two, three = tuple2
print(one)

def do_math (number1, number2):
    total = number1+number2
    product=number1 * number2
    return total, product

total, product = do_math(1,2)
print(total)
print(product)

def do_division(number1, number2):
    quotient = int(number1/number2)
    remainder = number1%number2
    return quotient, remainder

quotient, remainder = do_division(9,2)
print(quotient)
print(remainder)
