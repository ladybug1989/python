#1 import random
import random
#12 use while loop to ask player if want to play again
while True:
    #2 the choices that you are going to choose
    choices = ["rock", "paper", "scissors"]
    #6 initialize player
    player = None
    #3 against player
    computer = random.choice(choices)
    #5 while loop prevents player choose only rock,paper,scissors
    # inorder for the while loop to work need to initialize player to work
    while player not in choices:
    #4 player can type uppercase it will change to lower case and not give error
        player = input("rock, paper or scissors?: ").lower()
    #7 if player and computer chooses the same thing a tie
    if player == computer:
        print("player: ",player)
        print("computer: ",computer)
        print("tie!")
    #8 if statement
    #if player choose rock
    elif player == "rock":
        #9 nested if statement with different outcomes of what the computer choose
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("Lost!")
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("Win!")

    #10 if player choice scissors
    elif player == "scissors":
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("Win!")
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("Win!")

    #11 paper choice
    elif player == "paper":
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("lost!")
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("Win!")
    #13 ask the player to play again
    play_again = input("play again? (yes/no): ").lower()

    #14 if player does not like to play again then break statement means to stop
    if play_again != "yes":
        break
#15 Once while loop is broken the statement bye will show up 
print("Bye")