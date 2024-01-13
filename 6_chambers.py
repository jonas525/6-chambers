import random
import time 

#Russian roulette
Your_number = random.randrange(1,6)
Enemy_number = random.randrange(1,6)

x = int(input("Enter number: "))
y = random.randrange(1,6)

while x > 6 or x < 1:
    x = int(input("Enter number: "))
    

if x == Your_number:
    print("You die"  )
elif x != Your_number:
    print("You live")
    

time.sleep(1)


if y == Enemy_number:
    print("Enemy is dead")
elif y != Enemy_number:
    print("Enemy survive")

while y != Enemy_number and x != Your_number:
    x = int(input("Enter number: "))
    break
