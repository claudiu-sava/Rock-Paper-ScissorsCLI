import random
import os


def tryAgain(points):
    print("You reached " + str(points) + " points!")
    print("Wanna try again? y/n")
    choice = input()
    if choice == "y" or choice == "":
        os.system('cls' if os.name == 'nt' else 'clear')
        play(0)
    elif choice == "n":
        print("Exiting")
        exit()
    else:
        print("Unknown command. Exiting")
        tryAgain(points)


def goNext(points):
    print("Total points: " + str(points))
    print("Next round? y/n")
    choice = input()
    if choice == "y" or choice == "":
        os.system('cls' if os.name == 'nt' else 'clear')
        play(points)
    elif choice == "n":
        print("Exiting")
        exit()
    else:
        print("Unknown command. Exiting")


def draw(points):
    print("You still have " + str(points) + " points")
    print("Next round? y/n")
    choice = input()
    if choice == "y" or choice == "":
        os.system('cls' if os.name == 'nt' else 'clear')
        play(points)
    elif choice == "n":
        print("Exiting")
        exit()
    else:
        print("Unknown command. Try again")
        draw(points)


def play(points):
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    playerChoice = input(">> ")

    if playerChoice == "1" or playerChoice == "rock":
        playerChoice = "Rock"
    elif playerChoice == "2" or playerChoice == "paper":
        playerChoice = "Paper"
    elif playerChoice == "3" or playerChoice == "scissors":
        playerChoice = "Scissors"
    else:
      print("Unknown command. Try again")
      play(points)

    pcChoice = random.randint(1, 3)
    if pcChoice == 1:
        pcChoice = "Rock"
    elif pcChoice == 2:
        pcChoice = "Paper"
    elif pcChoice == 3:
        pcChoice = "Scissors"

    if playerChoice == "Rock" and pcChoice == "Rock":
        print("Draw")
        draw(points)
    elif playerChoice == "Rock" and pcChoice == "Paper":
        print("PC won!")
        tryAgain(points)
    elif playerChoice == "Rock" and pcChoice == "Scissors":
        print("You won!")
        points = points + 1
        goNext(points)
    elif playerChoice == "Paper" and pcChoice == "Rock":
        print("You won!")
        points = points + 1
        goNext(points)
    elif playerChoice == "Paper" and pcChoice == "Paper":
        print("Draw")
        draw(points)
    elif playerChoice == "Paper" and pcChoice == "Scissors":
        print("PC won!")
        tryAgain(points)
    elif playerChoice == "Scissors" and pcChoice == "Rock":
        print("PC won!")
        tryAgain(points)
    elif playerChoice == "Scissors" and pcChoice == "Paper":
        print("You won!")
        points = points + 1
        goNext(points)
    elif playerChoice == "Scissors" and pcChoice == "Scissors":
        print("Draw")
        draw(points)


play(0)
