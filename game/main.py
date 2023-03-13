import random


def choose_option():
    options = ("rock", "paper", "scissor")
    player = None
    while not player in options:
        player = input("rock, paper, scissor ->").lower()
        if not player in options:
            print("Choose the correct options")

    computer = random.choice(options)
    print("Player -> ", player)
    print("Computer ->", computer)
    return player, computer

def combat_check(player, computer, player_win, computer_win):
    if player == computer:
        print("You tie!")
    elif (player == "rock" and computer == "scissor") or (player == "scissor" and computer == "paper") or (player == "paper" and computer == "rock"):
        print("You win!")
        player_win += 1
    else:
        print("You lose!")
        computer_win += 1
    return player_win, computer_win
def check_winner(player_win, computer_win, round):
    if player_win == 3:
        print("\nTotal Rounds ->", round)
        print("You win! and Game Over")
        exit()
    elif computer_win == 3:
        print("\nYou loose! and Game Over")
        exit()


def run_game():
    player_win = 0
    computer_win = 0
    round = 1
    while True:
        print("*" * 15)
        print("ROUND" , round)
        print("*" * 15)

        print("Player => ",player_win)
        print("Computer => ",computer_win)

        check_winner(player_win, computer_win, round)

        player, computer = choose_option()
        player_win, computer_win = combat_check(player, computer, player_win, computer_win)
        round += 1

run_game()