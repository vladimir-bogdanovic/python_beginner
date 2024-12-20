import random

print("Welcome to hangman game!")

words = ["python", "java", "kotlin", "javascript", "computer", "programming", "science"]
word = random.choice(words)
print(word)

turns = len(word) + 2
correct_guesses = []


while turns > 0:
    display_word = ""
    for char in word:
        if char in correct_guesses:
            display_word += char + " "
        else:
            display_word += "_ "
    print(display_word)


    if "_ " not in display_word:
        print("grats, u win!")
        break

    guess = input("enter letter")

    if guess in correct_guesses:
        print("You already guessed this letter, choose another one.")
        continue

    if len(guess) >1 or not guess.isalpha():
        print("Yot must enter a valid letter and it must be 1 character.")

    if guess in word:
        correct_guesses +=guess
        print("Nice guess!")
    elif guess not in word:
        turns -= 1
        print(f"Wrong guess. You have {turns} left." )


