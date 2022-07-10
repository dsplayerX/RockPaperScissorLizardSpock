import random
from time import sleep

# Sheldon's Infamous Rock-Paper-Scissors-Lizard-Spock Game

options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

isRunning = True

while True:
    rand_index = random.randrange(len(options))
    compOption = options[rand_index]


    while True:
        userInput = input("\nSelect option: ")
        userOption = userInput.lower()

        if userOption in (i.lower() for i in options) or userOption == "q":
            break
        else:
            continue

    if userInput == "q":
        print("Quitting...")
        isRunning = False
        break
    else:
        print("# AI Sheldon selected " + compOption + ".")

        if userOption == "scissors" and compOption == "Paper":
            print("> You Win!")
        elif userOption == "paper" and compOption == "Rock":
            print("> You Win!")
        elif userOption == "rock" and compOption == "Lizard":
            print("> You Win!")
        elif userOption == "lizard" and compOption == "Spock":
            print("> You Win!")
        elif userOption == "spock" and compOption == "Scissors":
            print("> You Win!")
        elif userOption == "scissors" and compOption == "Lizard":
            print("> You Win!")
        elif userOption == "lizard" and compOption == "Paper":
            print("> You Win!")
        elif userOption == "paper" and compOption == "Spock":
            print("> You Win!")
        elif userOption == "spock" and compOption == "Rock":
            print("> You Win!")
        elif userOption == "rock" and compOption == "Scissors":
            print("> You Win!")
        else:
            print("> You Lose!")