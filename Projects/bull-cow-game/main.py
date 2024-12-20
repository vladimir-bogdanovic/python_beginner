import random

numbers_to_guess = {}
players_guess = []
players_guess_dict = {}

def generate_digits(digits):
    for key in range(4):
        while True:
            number = random.randrange(10)
            if number not in digits.values():
                digits[f"{key + 1}"] = number
                break

generate_digits(numbers_to_guess)
print(numbers_to_guess)


def input_validation(players_list):

    while True:
        players_input = input("Enter a combination: ")
        if not players_input.isdigit() or len(players_input) > 4:
            print("Enter a valid number with at most 4 digits.")
            continue
        elif len(set(players_input)) != len(players_input):  #set removes duplicate values
            print("All digits must be different. Try again.")
            continue
        else:
            break
    for digits in players_input:
        int_digits = int(digits)
        players_list.append(int_digits)
    return players_list

input_validation(players_guess)

def list_to_dict(dict, list):
    for key in range(4):
        dict[f"{key + 1}"] = list[key]
    return dict

list_to_dict(players_guess_dict,players_guess)


cows = 0
bulls = 0

for key, value in players_guess_dict.items():
    if value == numbers_to_guess[key]:  # Exact match at the correct position
        bulls += 1
        print(f"bull at position {key}")
    elif value in numbers_to_guess.values():  # Value exists but at a different position
        cows += 1
        print(f"cows : {cows}")

print(f"Total bulls: {bulls}, Total cows: {cows}")




