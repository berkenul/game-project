"""
Lab 1

This program allows the user to choose between two games:
a Guessing Game and Rock-Paper-Scissors. The user can play
either game multiple times, switch between games, or quit.

Group #: 11
Authors: [Alex Sett], [Berk Enul], [Han Bhone Hset]
Date: September 28, 2026
"""

import guessing
import rps


def display_welcome():
    """
    Display the welcome message and explain the available games.

    Author: [Alex Sett]
    """
    print("=" * 40)
    print("      Welcome to Arcade!      ")
    print("=" * 40)
    print("You may pick between the following games:")
    print("  1. Guessing Game: Try to guess the number that I'm thinking of within 5 tries!")
    print("  2. Rock-Paper-Scissors: Try and beat me in a game of rock-paper-scissors!")
    print("You can switch between games or play them multiple times.")
    print("=" * 40)


def main():
    """
    Run the main Arcade menu.

    Allow the user to pick a game or return to the main menu
    after playing, or quit the program.

    """
    display_welcome()

    while True:
        print("\nWhich game do you want to play?")
        print("1. Guessing Game")
        print("2. Rock-paper-scissors")
        print("3. Quit program")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            print("\n--- Starting Guessing Game ---")
            guessing.play_game()

        elif choice == "2":
            print("\n--- Starting Rock-Paper-Scissors ---")
            rps.play_game()

        elif choice == "3":
            print("\nThanks for playing! Goodbye.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        print("\n" + "-" * 40)

        switch_choice = input(
            "Do you want to play again or switch games? "
            "(Y to go back to the Main Menu, N to quit): "
        ).strip().upper()

        if switch_choice == "N":
            print("\nThanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()