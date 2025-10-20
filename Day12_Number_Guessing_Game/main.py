import random
import art
import sys

def generate_mystery_number():
    return random.randint(1, 100)

def difficulty():
    choice = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    attempt_count = 0
    valid_choice = False
    invalid_count = 0

    while not valid_choice:

        if choice == "easy":
            attempt_count = 10
            valid_choice = True
        elif choice == "hard":
            attempt_count = 5
            valid_choice = True
        else:
            if invalid_count < 3:
                choice = input("Invalid input. Please type 'easy' or 'hard': ").lower()
                invalid_count += 1
            elif invalid_count < 6:
                choice = input("Bruh. Quit playin'. 'easy' or 'hard': ")
                invalid_count += 1
            else:
                print("THAT'S IT! You had you're chance. I'm out.")
                sys.exit()

    return attempt_count

def guessed_num():
    input_num = int(input("Make a guess: "))
    if input_num not in range(1, 100):
        print("Guess must be between 1 and 100.")
        guessed_num()
    return int(input_num)

def play_game():
    mystery_number = generate_mystery_number()
    attempts = difficulty()

    while attempts > 0:
        guess = int(guessed_num())
        if guess > mystery_number:
            attempts -= 1
            print(f"Too high.\nGuess again.\nYou have {attempts} remaining.")
        elif guess < mystery_number:
            attempts -= 1
            print(f"Too low.\nGuess again.\nYou have {attempts} remaining.")
        elif guess == mystery_number:
            print(f"{mystery_number} is correct. You got it!!")
            break

        if attempts == 0:
            print(f"You lose. The number was {mystery_number}.")

    play_again = input("Would you like to play again? y/n: ")

    if play_again == "y":
        play_game()
    else:
        print("Thank you for playing!")
        sys.exit()

print(art.logo)
play_game()