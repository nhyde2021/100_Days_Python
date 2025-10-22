import art
from game_data import data
import random

def pull_data():
    return random.choice(data)

def initial_display(a, b):
    print(art.logo)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

def gameplay_display(result, a, b, score):
    if result:
        print(art.logo)
        print(f"You're right! Current score: {score}")
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(art.vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")

def submit_guess(a, b):
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    valid_input = False

    while not valid_input:
        if user_choice == 'a':
            user_choice = a
            valid_input = True
        elif user_choice == 'b':
            user_choice = b
            valid_input = True
        else:
            user_choice = input("Invalid input. Type 'A' or 'B': ")

    return user_choice

def compare(user, a, b):
    if a['follower_count'] > b['follower_count']:
            return user == a
    else:
        return user == b

def score_add(result, points):
    if result:
        points += 1
    return points

def play_game():
    score_total = 0
    game_over = False
    choice_a = pull_data()
    choice_b = pull_data()

    initial_display(choice_a, choice_b)

    while not game_over:
        while choice_a == choice_b:
            choice_b = pull_data()

        user_selection = submit_guess(choice_a, choice_b)
        compare_result = compare(user_selection, choice_a, choice_b)
        score_total = score_add(compare_result, score_total)

        if compare_result:
            choice_a = choice_b
            choice_b = pull_data()
            gameplay_display(compare_result, choice_a, choice_b, score_total)
        else:
            gameplay_display(compare_result, choice_a, choice_b, score_total)
            play_again = input("Would you like to play again? y/n: ")
            if play_again == "y":
                play_game()
            else:
                game_over = True

play_game()