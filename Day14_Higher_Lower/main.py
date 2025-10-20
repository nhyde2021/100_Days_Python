import art
from game_data import data
import random

#TODO: Create a function for pulling two random items from game data setting them to A and B.
def pull_data():
    return random.choice(data)

#TODO: Compare the two and determine which has more searches.
def display():
    choice_a = pull_data()
    choice_b = pull_data()

    if choice_a['name'] == choice_b['name']:
        choice_b = pull_data()

    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(art.vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
#TODO: Increment a score counter by one with each correct guess and the correct choice is to be compared to the next.
#TODO: End game and display score upon an incorrect guess.

choice_a = None
choice_b = None

