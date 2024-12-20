import random


def pick_first_number():
    while True:
        try:
            first_number = int(input("Enter first number: "))
            if first_number > 0:
                print("Valid number entered:", first_number)
                return first_number
            else:
                print("You must enter a positive number.")
        except ValueError:
            print("That's not a valid integer. Try again.")

first_num = pick_first_number()


def pick_second_number():
    while True:
        try:
            second_number = int(input("Enter second number: "))
            if second_number > 0 and second_number > first_num + 10:
                print("Valid number entered:", second_number)
                return second_number  # Return the validated integer
            else:
                print("You must enter a positive number and value must be bigger for at least 10 than first number.")
        except ValueError:
            print("That's not a valid integer. Try again.")
second_num = pick_second_number()

def generate_random_number():
    guess_number_float = random.uniform(first_num, second_num + 1)
    guess_number = int(guess_number_float)
    return guess_number

winning_num = generate_random_number()
print(winning_num)




guess_count = 0
guess_chances = 5
while guess_count < guess_chances:
    try:
        player_guess = int(input("guess number"))
        guess_count += 1
        if player_guess == winning_num:
                print("Congratulations, you won the game!")
                break
        elif guess_count >= guess_chances and player_guess != winning_num:
                print("You lost!")
        elif player_guess > winning_num :
                print("Your guess is to high, try again")
        elif player_guess < winning_num:
                print("Your guess is to low, try again")
    except ValueError:
        print("You need to enter valid number")
