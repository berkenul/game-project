# Lab 1
# Group #: 11
# Authors: Berk Enul
# Date: September 28, 2026

import random


def play_game():
    """Play one round with a number from 1 to 100 and five valid guesses.

    Give high/low hints and reveal the number if the player loses.
    Author: Berk Enul.
    """
    number = random.randint(1, 100)
    tries_left = 5
    print("I'm thinking of a number between 1 and 100.")

    while tries_left > 0:
        try:
            guess = int(input(f"Guess what it is ({tries_left} tries left): "))
        except ValueError:
            print("Please enter a whole number between 1 and 100.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        tries_left -= 1
        if guess == number:
            print("You got it!")
            return
        if tries_left == 0:
            print(f"Nope! You lost. The number was {number}.")
        elif guess < number:
            print("Nope! Too low. Try again.")
        else:
            print("Nope! Too high. Try again.")


if __name__ == "__main__":
    while True:
        play_game()
        answer = input("Do you want to play again? (Y/N): ").strip().lower()
        if answer not in ("y", "yes"):
            break
