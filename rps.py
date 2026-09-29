# Lab 1
# Group #: 11
# Authors: Han Bhone Hset
# Date: September 28, 2026

import random

NAMES = {1: "paper", 2: "scissors", 3: "rock"}
PLAYER_WINS = {(1, 3), (2, 1), (3, 2)}


def play_game():
    """Play one round against a random computer choice and report the result.

    Author: Han Bhone Hset.
    """
    computer = random.randint(1, 3)

    while True:
        choice = input("Enter your choice: 1. paper, 2. scissors, 3. rock: ").strip()
        if choice in ("1", "2", "3"):
            player = int(choice)
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    print(f"You chose {NAMES[player]}; the computer chose {NAMES[computer]}.")

    if player == computer:
        print("It is a tie!")
    elif (player, computer) in PLAYER_WINS:
        print(f"You win! {NAMES[player].capitalize()} beats {NAMES[computer]}.")
    else:
        print(f"I win! {NAMES[computer].capitalize()} beats {NAMES[player]}.")


if __name__ == "__main__":
    answer = input("Do you want to play? ").strip().lower()
    while answer in ("y", "yes"):
        play_game()
        answer = input("Do you want to play again? (Y/N) ").strip().lower()
