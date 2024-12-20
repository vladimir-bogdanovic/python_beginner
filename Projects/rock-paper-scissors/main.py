import random

choices = ["rock","paper","scissors","r","p","s"]

computer_choice = random.choice(choices)
def converting_into_full_word(x):
    if x == "r":
        x = "rock"
    elif x == "p":
        x = "paper"
    elif x == "s":
        x = "scissors"
    else:
        x = x
    return x

computer_choice_full = converting_into_full_word(computer_choice)

while True:
    players_input = input("Choose rock, paper, scissors (or r, p, s): ")
    players_choice = players_input.lower()

    if players_choice not in choices:
         print(f"You must choose some of these choices: {choices}")
    else:
         break

players_choice_full = converting_into_full_word(players_choice)

print("You have chosen: ",players_choice_full)
print("Computer have chosen: ",computer_choice_full)

if players_choice_full == computer_choice_full:
    print("It's a tie!")
elif players_choice_full == "paper" and computer_choice_full == "scissors":
    print("U lost!")
elif players_choice_full == "paper" and computer_choice_full == "rock":
    print("U win!")
elif players_choice_full == "rock" and computer_choice_full == "scissors":
    print("U win!")
elif players_choice_full == "rock" and computer_choice_full == "paper":
    print("U lost!")
elif players_choice_full == "scissors" and computer_choice_full == "paper":
    print("U won!")
elif players_choice_full == "scissors" and computer_choice_full == "rock":
    print("U lost!")
