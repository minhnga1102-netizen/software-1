import random
#N
random_points = int(input("How many random points to generate? "))
#n
points_inside_circleA = 0

count = 0

#function uniform: float number -1,1
while count < random_points:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <1: 
        points_inside_circleA +=1
    count +=1

print(f"Approximation of pi: {4*points_inside_circleA/random_points}")
