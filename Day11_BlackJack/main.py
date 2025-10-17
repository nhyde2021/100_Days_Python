import random
import sys
from operator import indexOf

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def initial_deal(player, dealer):
    player.append(random.choice(cards))
    player.append(random.choice(cards))
    dealer.append(random.choice(cards))

def hit(hand):
    hand.append(random.choice(cards))

def play_blackjack():

    player_hand = []
    dealer_hand = []
    initial_deal(player_hand, dealer_hand)


    if sum(player_hand) > 21:
        player_hand[-1] = 1

    board = f"Your hand: {player_hand}            Dealer hand: {dealer_hand}"
    print(board)

    while sum(player_hand) < 22:
        hit_stay = input(f"You have {sum(player_hand)} would you like to hit or stay: ").lower()
        if hit_stay == "hit":
            hit(player_hand)
            print(f"\n**********You were dealt a {player_hand[-1]}**********\n")
            if sum(player_hand) > 21 and 11 in player_hand:
                ace_index = indexOf(player_hand, 11)
                player_hand[ace_index] = 1
        elif hit_stay == "stay":
            break
        else:
            print("Please type 'hit' or 'stay'")
    if sum(player_hand) > 21:
        print(f"{sum(player_hand)}, BUST!")
    else:

        while sum(dealer_hand) < 17:
            hit(dealer_hand)
            print(f"**********Dealer was dealt a {dealer_hand[-1]}**********")
            if sum(dealer_hand) > 21 and 11 in dealer_hand:
                ace_index = indexOf(dealer_hand, 11)
                dealer_hand[ace_index] = 1


        if sum(dealer_hand) > 21:
            print(f"{sum(player_hand)} vs. {sum(dealer_hand)} Dealer busts, You Win!!")
        elif sum(player_hand) > sum(dealer_hand):
            print(f"{sum(player_hand)} vs. {sum(dealer_hand)} You WIN!!")
        elif sum(player_hand) == sum(dealer_hand):
            print(f"{sum(player_hand)} vs. {sum(dealer_hand)} it's a push.")
        else:
            print(f"{sum(player_hand)} vs. {sum(dealer_hand)} Dealer Wins.")

    another_game = input("Deal again? y/n: ")

    if another_game == "n":
        sys.exit()
    elif another_game == "y":
        play_blackjack()
print(art.logo)
play_blackjack()

#TODO: Add functionality for Aces being 1 or 11 based on hand total

