import random
from time import sleep
from ascii_gestures import *

# Sheldon's Infamous Rock-Paper-Scissors-Lizard-Spock Game

options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

compCount = 0
playerCount = 0

isRunning = True

while True:
    rand_index = random.randrange(len(options))
    compOption = options[rand_index]
    #print(compOption)

    while True:
        print('''
------------
 R. Rock
 P. Paper
 S. Scissors
 L. Lizard
 SP. Spock
------------
 H. Help
 Q. Quit''')
        userInput = input("\nSelect option: ")
        userOption = userInput.lower()

        userInputOptions = ["rock", "paper", "scissors", "lizard", "spock", "quit", "help", "r", "p", "s", "l", "sp", "q", "h"]

        if userOption in userInputOptions:
            if userOption == "r" or userOption == "rock":
                userOption = "Rock"
            if userOption == "p" or userOption == "paper":
                userOption = "Paper"
            if userOption == "s" or userOption == "scissors":
                userOption = "Scissors"
            if userOption == "l" or userOption == "lizard":
                userOption = "Lizard"
            if userOption == "sp" or userOption == "spock":
                userOption = "Spock"
            break
        else:
            print("\n> Wrong input! Try again!")
            continue

    if userOption == "q" or userOption == "quit":
        print("\n> You won " + str(playerCount) + " time(s)!")
        sleep(1)
        print("\n> AI Sheldon won " + str(compCount) + " time(s)!")
        sleep(3)
        print("\nQuitting...")
        sleep(1)
        isRunning = False
        break

    elif userOption == "h" or userOption == "help":
        print(
'''
Scissors cuts Paper, 
Paper covers Rock, 
Rock crushes Lizard, 
Lizard poisons Spock, 
Spock smashes Scissors, 
Scissors decapitates Lizard, 
Lizard eats Paper, 
Paper disproves Spock, 
Spock vaporizes Rock, 
and as it always has, 
Rock crushes Scissors.
    - Sheldon L. Cooper, BBT
''')
        continue
    else:
        print("\n# You picked " + userOption + ".")
        printGesture(userOption)
        print("\n# AI Sheldon selected " + compOption + ".")
        printGesture(compOption)


        if userOption == "Scissors" and compOption == "Paper":
            print("> You Win!")
            playerCount += 1
        elif userOption == "Paper" and compOption == "Rock":
            print("> You Win!")
            playerCount += 1
        elif userOption == "Rock" and compOption == "Lizard":
            print("> You Win!")
            playerCount += 1
        elif userOption == "Lizard" and compOption == "Spock":
            print("> You Win!")
            playerCount += 1
        elif (userOption == "Spock") and compOption == "Scissors":
            print("> You Win!")
            playerCount += 1
        elif userOption == "Scissors" and compOption == "Lizard":
            print("> You Win!")
            playerCount += 1
        elif userOption == "Lizard" and compOption == "Paper":
            print("> You Win!")
            playerCount += 1
        elif userOption == "Paper"  and compOption == "Spock":
            print("> You Win!")
            playerCount += 1
        elif userOption == "Spock" and compOption == "Rock":
            print("> You Win!")
            playerCount += 1
        elif userOption == "Rock" and compOption == "Scissors":
            print("> You Win!")
            playerCount += 1
        elif userOption == compOption:
            print("> Tie!")
        else:
            print("> You Lose!")
            compCount += 1
        print("------------")

