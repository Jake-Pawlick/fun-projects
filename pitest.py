# A program that estimates the value of pi by simulating X amount of points and checking to see how many fall within a circular range
import random 
import math
listx = []
listy = []
incirc = 0
points = int(input("how many points do you want to generate?: "))
for i in range(points):
    listx.append(random.random())
    listy.append(random.random())
for i in range(points):
    squarx = [n ** 2 for n in listx]
    squary = [n ** 2 for n in listy]
    final = [a + b for a, b in zip(squarx, squary)]
for number in final:
    if number <= 1:
        incirc += 1
    else:
        pass
pitest = 4 * (incirc / points)
difference = abs(pitest - math.pi)
print("The pi test is: ", pitest)
print("The difference between pi and the pi test is: ", difference)