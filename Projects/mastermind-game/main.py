import random
from os.path import split

computer_choices = ["1","2","3","4","5","6","7","8","9","0"]
computer_guessed_digits = []

player_guessed_digits = []

players_guesses = 0
computer_guesses = 0

# while True:
#     user_input = input("Enter a number: ")
#     try:
#         number = int(user_input)
#         break
#     except ValueError:
#         print("Invalid input. Please enter an integer.")
#         continue
#
# stripped_user_input = user_input.strip()
# print(f"You set number {stripped_user_input}")
#
#
# def splitting_number(num):
#     return list(num)
#
# players_digits = splitting_number(stripped_user_input)
# print(players_digits, "ovo su cifre unutar broja igraca")
#
#
# while sorted(computer_guessed_digits) != sorted(players_digits):
#     computer_guesses +=1
#     try:
#         com_guess = random.choice(computer_choices)
#         computer_choices.remove(com_guess)
#         for digit in players_digits:
#             if digit == com_guess:
#                 computer_guessed_digits.append(com_guess)
#             # else:
#             #     print("nema poklapanja")
#     except ValueError as e:
#         print("Something went wrong:", e)
#         break
#
# print(f"Computer needed {computer_guesses} guesses to guess your number.")

# players turn

import random

# Generate a random number and convert it to a string
number_to_guess = random.randint(1, 99999)
number_to_guess_str = str(number_to_guess)
print(f"Number to guess (for testing): {number_to_guess}")  # For debugging


print("Players turn")

while len(player_guessed_digits) < len(number_to_guess_str):
    # Get player input
    player_input = input("Enter a number (0-9): ")

    # Validate input
    if len(player_input) != 1 or not player_input.isdigit():
        print("Invalid input. You must enter a single digit from 0 to 9.")
        continue

    # Check if the guessed digit exists in the number
    found = False
    for index, digit in enumerate(number_to_guess_str):
        if digit == player_input and (player_input, index) not in player_guessed_digits:
            player_guessed_digits.append((player_input, index))
            print(f"Number {player_input} exists at index {index}")
            found = True

    if not found:
        print(f"Number {player_input} does not exist in the number.")

    # Display progress
    guessed_progress = ''.join(
        [digit if (digit, idx) in player_guessed_digits else '_' for idx, digit in enumerate(number_to_guess_str)])
    print(f"Current progress: {guessed_progress}")

print("Congratulations! You guessed the number.")



