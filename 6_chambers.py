import random 

x = int(input("Enter number: "))
y = random.randrange(1,6)

Your_number = random.randrange(1,6)
Enemy_number = random.randrange(1,6)

while x > 6 or x < 1:
    print("You can only chose from 1 to 6. Try again:  ")

def game(Your_number, Enemy_number):
    if x == Your_number and y != Enemy_number:
        print("Enemy is dead")
    elif x != Your_number and y == Enemy_number:
        print("Enemy survive, you are dead")
    elif x == Your_number and y == Enemy_number:
        print("Bullets collided in flight")
    elif x != Your_number and y != Enemy_number:
        print("Both of you missed")
    else:
        print("ERROR, try again" )


    Your_number = random.randrange(1,6)
    Enemy_number = random.randrange(1,6)


while True: 
    x = int(input("Enter number: "))
    result = game(Your_number, Enemy_number,)

    if result in ["Enemy is dead", "Enemy survive, you are dead"]:
         break
