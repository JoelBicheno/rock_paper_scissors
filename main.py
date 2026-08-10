#----- Main Code -----

import random

def game(total_games):
    games_played = 0
    score = 0
    computer_choice = ""
    user_choice = ""
    while games_played < int(total_games):
        games_played += 1
        computer_choice = "a"
        user_choice = "a"
        while computer_choice == user_choice:
            user_choice = input("Please choose rock, paper or scissors: ")
            user_choice = user_choice.lower()
            while user_choice not in ["rock", "paper", "scissors"]:
                print("Invalid choice")
                user_choice = input("Please choose rock, paper or scissors: ")
                user_choice = user_choice.lower()
            computer_choice = random.choice(["rock", "paper", "scissors"])
            if user_choice == computer_choice:
                print("Draw you both chose:", user_choice)
        print("The computer chose", computer_choice)
        if (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "rock"):
            print("You lost!")
        else:
            print("You Won!")
            score += 1
        print()
    print("You won", score, "/", games_played, "rounds.")

#----- Game UI -----

play_again = True

while play_again:
    print()
    print("Let's play Rock, Paper, Scissors!")
    print()
    total_games = input("How many rounds would you like to play? ")
    print()
    game(total_games)
    user_continue = input("Would you like to play again (yes or no)? ")
    while user_continue.lower() not in ["yes", "no"]:
        print("Not a valid choice.")
        user_continue = input("Would you like to play again (yes or no)? ")
    if user_continue.lower() == "no":
        play_again = False

print()
print("Thank you for playing Rock, Paper, Scissors!")
print()