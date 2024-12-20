import random
from types import new_class

cards = []
ranks = [
          {"rank" : "A", "value" : 11},
          {"rank" : "2", "value" : 2},
          {"rank" : "3", "value" : 3},
          {"rank" : "4", "value" : 4},
          {"rank" : "5", "value" : 5},
          {"rank" : "6", "value" : 6},
          {"rank" : "7", "value" : 7},
          {"rank" : "8", "value" : 8},
          {"rank" : "9", "value" : 9},
          {"rank" : "10", "value" : 10},
          {"rank" : "J", "value" : 10},
          {"rank" : "Q", "value" : 10},
          {"rank" : "K", "value" : 10}
        ]
suits = ["spades", "diamonds", "hearts", "clubs"]

def create_deck():
    for card in ranks:
        for suit in suits:
          deck = f"{card['rank']} of {suit}"
          cards.append(deck)

create_deck()
random.shuffle(cards)

def deal_cards(number):
    dealt_cards = []
    value = 0
    aces = 0
    for x in range(number):
        dealt_cards.append(cards.pop())
    for card in dealt_cards:
        split_card = card.split()[0]

        for rank in ranks:
            if rank["rank"] == split_card:
                value += rank["value"]
                if split_card == "A":
                    aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return dealt_cards, value

players_cards = deal_cards(2)
dealers_cards = deal_cards(2)

def display_cards():
    print(f"Player's cards: {players_cards[0]} (Value: {players_cards[1]})")
    print(f"Dealer's cards: {dealers_cards[0][0]} and [Hidden]")

players_cards_total = players_cards[1]
dealers_cards_total = dealers_cards[1]

display_cards()

while True:
    if dealers_cards_total == 21 and players_cards_total != 21:
        print("Dealer got Blackjack! You lose!")
        break
    elif players_cards_total == 21 and dealers_cards_total != 21:
        print("You hit Blackjack! You win!")
        break

    # Player's turn
    player_input = input("Hit or Stand? (H/S): ").strip().lower()
    if player_input in ['h', 'hit']:
        new_player_card = deal_cards(1)
        players_cards[0].extend(new_player_card[0])
        players_cards_total += new_player_card[1]

        print(f"You drew {new_player_card[0][0]}. Total value: {players_cards_total}")

        if players_cards_total > 21:
            print("You busted! Dealer wins.")
            break
        elif players_cards_total == 21:
            print("You hit Blackjack! You win!")
            break

    elif player_input in ['s', 'stand']:
        print("Player stands. Dealer's turn.")
        print(f"Dealer's cards: {dealers_cards[0]} (Value: {dealers_cards_total})")

        # Dealer's turn
        while dealers_cards_total < 17:
            new_dealer_card = deal_cards(1)
            dealers_cards[0].extend(new_dealer_card[0])
            dealers_cards_total += new_dealer_card[1]

            print(f"Dealer drew {new_dealer_card[0][0]}. Total value: {dealers_cards_total}")

            if dealers_cards_total > 21:
                print("Dealer busted! You win!")
                break

        if dealers_cards_total <= 21:
            if dealers_cards_total > players_cards_total:
                print("Dealer wins!")
            elif dealers_cards_total < players_cards_total:
                print("You win!")
            else:
                print("It's a tie!")
        break
    else:
        print("Invalid input. Please choose 'Hit' or 'Stand'.")