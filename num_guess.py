#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Oct. 15th, 2023
# This program asks the user to guess a number between 0 and 9
# and tells the user if they got it correct.
import constants


def main():
    # Get the user's guess
    user_guess = int(input("Guess a number between 0 and 9: "))

    # Check if the user's guess is correct
    if constants.CORRECT_GUESS == user_guess:
        print("You have guessed the correct number!")

    # Check if the user's guess is incorrect
    if constants.CORRECT_GUESS != user_guess:
        print("You have guessed incorrectly.")
        print("Please try again.")


if __name__ == "__main__":
    main()
