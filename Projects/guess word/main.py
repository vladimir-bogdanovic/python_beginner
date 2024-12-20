import random

random_words = ["cat", "dog", "mouse", "lion", "sheep"]
word = random.choice(random_words)

turns = 10
guesses = ""

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            failed += 1
            print("_")

    if failed == 0:
        print("Victory!")
        print("The word is: ", word)
        break

    print()
    guess = input("enter your guess")
    if(len(guess) > 1):
        print("U can only enter 1 letter")
        continue
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have", turns, 'more guesses left')

        if turns == 0:
            print("You Lose! The word was:", word)
#
