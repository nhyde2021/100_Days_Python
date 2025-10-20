import random
import sys
import art

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(CARDS)

def calculate_hand_value(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10  # Convert Ace from 11 to 1
        aces -= 1
    return total

def initial_deal(player, dealer):
    player.extend([deal_card(), deal_card()])
    dealer.append(deal_card())

def display_hands(player, dealer, reveal_dealer=False):
    dealer_display = dealer if reveal_dealer else [dealer[0], '?']
    print(f"\nYour hand: {player} (Total: {calculate_hand_value(player)})")
    print(f"Dealer hand: {dealer_display}\n")

def player_turn(player_hand):
    while calculate_hand_value(player_hand) < 21:
        choice = input("Would you like to hit or stay? ").strip().lower()
        if choice == "hit":
            card = deal_card()
            player_hand.append(card)
            print(f"\nYou were dealt a {card}")
            display_hands(player_hand, dealer_hand)
        elif choice == "stay":
            break
        else:
            print("Invalid input. Please type 'hit' or 'stay'.")
    return calculate_hand_value(player_hand)

def dealer_turn(dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        card = deal_card()
        dealer_hand.append(card)
        print(f"Dealer was dealt a {card}")
    return calculate_hand_value(dealer_hand)

def determine_winner(player_total, dealer_total):
    print(f"\nFinal Hands:")
    display_hands(player_hand, dealer_hand, reveal_dealer=True)

    if player_total > 21:
        print("You busted. Dealer wins.")
    elif dealer_total > 21:
        print("Dealer busted. You win!")
    elif player_total > dealer_total:
        print("You win!")
    elif player_total == dealer_total:
        print("It's a push.")
    else:
        print("Dealer wins.")

def play_blackjack():
    global player_hand, dealer_hand
    player_hand = []
    dealer_hand = []

    initial_deal(player_hand, dealer_hand)
    display_hands(player_hand, dealer_hand)

    player_total = player_turn(player_hand)
    if player_total <= 21:
        dealer_total = dealer_turn(dealer_hand)
    else:
        dealer_total = calculate_hand_value(dealer_hand)

    determine_winner(player_total, dealer_total)

    if input("\nDeal again? (y/n): ").strip().lower() == "y":
        play_blackjack()
    else:
        print("Thanks for playing!")
        sys.exit()

# Start the game
print(art.logo)
play_blackjack()
