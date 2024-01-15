6-Chambers Game
Description

This is a simple console-based game called "6-Chambers". It is a shooting game that involves players selecting a number between 1 and 6 to represent the chamber in which they believe a bullet is loaded. The game supports both single-player and two-player modes.
Requirements

    Python 3.x

How to Play
Single-player mode

    The player is prompted to enter a number between 1 and 6.
    A random number is generated for both the player and the enemy.
    If the player's chosen number matches the generated number, the enemy is defeated. If not, the enemy survives.
    The game continues until there is a winner.

Two-player mode

    Player 1 and Player 2 are prompted to enter their respective numbers between 1 and 6.
    Random numbers are generated for both players.
    The game logic determines the outcome: whether Player 2 defeats Player 1, Player 1 defeats Player 2, bullets collide in flight, or both players miss.
    The game continues until there is a winner.

How to Run

    Download the code from https://github.com/jonas525/6-chambers.
    Ensure you have Python 3.x installed.
    Execute the code in a Python environment.

Game Design

The game has a simple ASCII art logo displayed at the beginning.

plaintext

------------------------------------------------------
╔═══╗    ╔═══╗╔╗           ╔╗
║╔══╝    ║╔═╗║║║           ║║
║╚══╗    ║║ ╚╝║╚═╗╔══╗ ╔╗╔╗║╚═╗╔══╗╔═╗╔══╗
║╔═╗║    ║║ ╔╗║╔╗║╚ ╗║ ║╚╝║║╔╗║║╔╗║║╔╝║══╣
║╚═╝║    ║╚═╝║║║║║║╚╝╚╗║║║║║╚╝║║║═╣║║ ╠══║
╚═══╝    ╚═══╝╚╝╚╝╚═══╝╚╩╩╝╚══╝╚══╝╚╝ ╚══╝
Game created by jonas525
Dowloaded form: https://github.com/jonas525/6-chambers
------------------------------------------------------

Main Game Loop

    The game starts with a menu that allows the player to choose between single-player, two-player, or exit the game.
    The player is prompted to enter their choice (1, 2, or 3).
    The respective function is called based on the player's choice.
    The game loop continues until the player chooses to exit.

Credits

    Game created by jonas525

Feel free to download and enjoy playing the game!
