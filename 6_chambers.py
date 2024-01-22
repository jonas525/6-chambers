import random 
import time
import sys

# Function for the single-player game
def player1 ():
    # Get user input for the player's number'
    Your_number = int(input("Enter number: "))
    # Generate random number for the player and enemy
    number = random.randrange(1,6)
    Enemy_number = random.randrange(1,6)

    # Validate user input
    while Your_number > 6 or Your_number < 1:
        Your_number = int(input("You can only chose from 1 to 6. Try again:  "))
    
    # Define the game logic function
    def game(Your_number, Enemy_number):
        if Your_number == number and Enemy_number != number:
            print("Enemy is dead")
        elif Your_number != number and Enemy_number == number:
            print("Enemy survive, you are dead")
        elif Your_number == number and Enemy_number == number:
            return "Bullets collided in flight"
        elif Your_number != number and Enemy_number != number:
            return "Both of you missed"
        else:
            print ("ERROR, try again")
        print ("Game Over")
    
    # Get the final score and continue the game until there is a winner
    final_score = game(Your_number, Enemy_number)

    while Your_number != number and Enemy_number != number or Your_number == number and Enemy_number == number:
        final_score = game(Your_number, Enemy_number)
        print(final_score)
        Your_number = int(input("Enter a number: "))
        if Your_number == number:
            final_score = game(Your_number, Enemy_number)
            print(final_score)
            break
        
         
    return final_score




# Function for the two-player game
def player2 ():
    # Get input for players and generate random number
    Your_number = int(input("Player_1: Enter number: "))
    Enemy_number = int(input("Player_2: Enter number: "))
    number = random.randrange(1,6)


    # Validate user inputs
    while Your_number > 6 or Your_number < 1:
        Your_number = int(input("You can only chose from 1 to 6. Try again:  "))


    while Enemy_number > 6 or Enemy_number < 1:
        Enemy_number = int(input("You can only chose from 1 to 6. Try again:  "))

    # Define the game logic function        
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
             print ("ERROR, try again")
        print ("Game Over")

    # Get the final score
    final_score = game(Your_number, Enemy_number)

    while Your_number != number and Enemy_number != number or Your_number == number and Enemy_number == number:
        final_score = game(Your_number, Enemy_number)
        print(final_score)
        time.sleep(1)
        Your_number = int(input("Player_1: Enter a number: "))
        time.sleep(0.5)
        Enemy_number = int(input("Player_2: Enter a number: "))
        if Your_number == number or Enemy_number == number:
            final_score = game(Your_number, Enemy_number)
            break   
    return final_score


# Main game loop


print("------------------------------------------------------")
print("╔═══╗    ╔═══╗╔╗           ╔╗")
print("║╔══╝    ║╔═╗║║║           ║║")
print("║╚══╗    ║║ ╚╝║╚═╗╔══╗ ╔╗╔╗║╚═╗╔══╗╔═╗╔══╗")
print("║╔═╗║    ║║ ╔╗║╔╗║╚ ╗║ ║╚╝║║╔╗║║╔╗║║╔╝║══╣")
print("║╚═╝║    ║╚═╝║║║║║║╚╝╚╗║║║║║╚╝║║║═╣║║ ╠══║")
print("╚═══╝    ╚═══╝╚╝╚╝╚═══╝╚╩╩╝╚══╝╚══╝╚╝ ╚══╝")
print("Game created by jonas525")
print("Downloaded from: https://github.com/jonas525/6-chambers")
print("------------------------------------------------------")
while True:
    time.sleep(1)
    print("------------------------------------------------------")
    print("Game for one player (1)")
    print("Game for two players (2)")
    print("Exit the game (3)")
    Select_a_type_of_game = int(input("Chose game: "))
    print("------------------------------------------------------")


    if Select_a_type_of_game == 1:
        player1()
    elif Select_a_type_of_game  == 2:
        player2()
    elif Select_a_type_of_game == 3:
        sys.exit()
    else:
        print("Error")
