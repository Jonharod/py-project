# iniciando juego
import random

def run_game():
    options = ("rock","paper","scissor","lizard","spock")
    computer = "rock"
    player = None


    while player not in options:
        player = input("Enter your choice->")

    print(f"player ->{player}")
    print(f"computer ->{computer}")

    combat(player,computer)
def combat(player,computer):
    if player == computer:
        print("tie!")
    elif (player == "rock" and computer == "scissor" or "lizard") or\
        (player == "paper" and computer == "rock" or "spock") or\
        (player == "scissor" and computer == "paper" or "lizard") or\
        (player == "lizard" and computer == "paper" or "spock") or\
        (player == "spock" and computer == "rock" or "scissor"):
        print("player win!")
    else:
        print("computer win!")


run_game()

                        




