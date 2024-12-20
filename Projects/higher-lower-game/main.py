import  random
from game_data import data

profiles = data

def get_profile():
    return random.choice(profiles)

score = 0
p1 = get_profile()
p2 = get_profile()

def show_celebrities(c1, c2, score):
    playing = True
    while playing:
        while c1 == c2:
            c2 = get_profile()

        print(f"Celebrity number 1 is {c1["name"]}.\n"
              f"Celebrity number 2 is {c2["name"]}.")

        answer = input(f"Does {c1["name"]} have more followers than {c2["name"]}?")

        if answer == "y" and c1["follower_count"] > c2["follower_count"]:
            c2 = get_profile()
            score += 1
            print("That's correct answer!")
        elif answer == "n" and c2["follower_count"] > c1["follower_count"]:
            c1 = c2
            c2 = get_profile()
            score += 1
            print("That's correct answer!")
        else:
            print(f"That's incorrect answer! Your score is {score}.")
            playing = False
    return score


def game():
    print("This is the game where you will be shown 2 celebrities.\nGoal is to guess if celebrity 1 has more followers than celebrity 2 on instagram.")
    print("Your choices will be 'yes' or 'no' (y/n).")

    while True:
        player_input = input("Do you want to start the game? ")
        if player_input.lower() == "y" or player_input.lower() == "yes":
                show_celebrities(p1,p2,score)
                # os.system("cls")
                break
        elif player_input.lower() == "n" or player_input.lower() == "no":
                print("Exiting game")
                break
        else:
                print("Enter valid input. Your choices are 'yes' or 'no' (y/n).")
                continue


game()