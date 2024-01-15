import random 
import time
import sys


def player1 ():
    Your_number = int(input("Enter number: "))
    number = random.randrange(1,6)
    Enemy_number = random.randrange(1,6)


    while Your_number > 6 or Your_number < 1:
        Your_number = int(input("You can only chose from 1 to 6. Try again:  "))

    def game(Your_number, Enemy_number):
        if Your_number == number and Enemy_number != number:
            print("Enemy is dead")
        elif Your_number != number and Enemy_number == number:
            print("Enemy survive, you are dead")
        elif Your_number == number and Enemy_number == number:
            return ("Bullets collided in flight")
        elif Your_number != number and Enemy_number != number:
            return ("Both of you missed")
        else:
            return "ERROR, try again"

    final_score = game(Your_number, Enemy_number)

    while Your_number != number and Enemy_number != number or Your_number == number and Enemy_number == number:
        final_score = game(Your_number, Enemy_number)
        print(final_score)
        Your_number = int(input("Enter a number: "))
        if Your_number == number:
            final_score = game(Your_number, Enemy_number)
            break
        return final_score




def player2 ():
    Your_number = int(input("Player_1: Enter number: "))
    number = random.randrange(1,6)
    Enemy_number = int(input("Player_2: Enter number: "))


    while Your_number > 6 or Your_number < 1:
        Your_number = int(input("You can only chose from 1 to 6. Try again:  "))


    while Enemy_number > 6 or Enemy_number < 1:
        Enemy_number = int(input("You can only chose from 1 to 6. Try again:  "))

    def game(Your_number, Enemy_number):
        if Your_number == number and Enemy_number != number:
            print("Player_2 is dead")
        elif Your_number != number and Enemy_number == number:
            print("Player_2 survive, Player_1 is dead")
        elif Your_number == number and Enemy_number == number:
            return "Bullets collided in flight"
        elif Your_number != number and Enemy_number != number:
            return "Both of you missed"
        else:
            return "ERROR, try again"


    final_score = game(Your_number, Enemy_number)

    while Your_number != number and Enemy_number != number or Your_number == number and Enemy_number == number:
        final_score = game(Your_number, Enemy_number)
        print(final_score)
        Your_number = int(input("Player_1: Enter a number: "))
        Enemy_number = int(input("Player_2: Enter a number: "))
        if Your_number == number or Enemy_number == number:
            final_score = game(Your_number, Enemy_number)
            break
        
       
    return final_score

while True:
    print("Game for one player (1)")
    print("Game for two players (2)")
    print("Exit the game (3)")
    Select_a_type_of_game = int(input("Chose game: "))

    if Select_a_type_of_game == 1:
        player1()
    elif Select_a_type_of_game  == 2:
        player2()
    elif Select_a_type_of_game == 3:
        sys.exit()
    else:
        print("Error")
