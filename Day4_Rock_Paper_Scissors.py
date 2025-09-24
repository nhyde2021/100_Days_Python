import random

rock = '''       
        ,--.--._
------"  _, ___)
        / _/____)
        //(____)
------     (__)
       `-----"
       '''
paper = '''

       ,--.--.______
------" _,  ___)_____)
            __________)
            _________)
------      ______)
       `-----"
       '''
scissors = ''' 
       ,--.--.______
------" _,  ___)_____)
            __________)
            (____)
------     (____)
       `-----"
        '''
options = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!\n")
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
computer_choice = random.randint(0, 2)

while player_choice not in ['0', '1', '2']:
    print("Invalid input! Try again.")
    player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

print(f"\nYou chose:\n{options[int(player_choice)]}")
print(f"Computer chose:\n{options[int(computer_choice)]}\n")

if player_choice == '0':
    
    if computer_choice == 0:
        print("It's a draw!")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")

elif player_choice == '1':
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("It's a draw!")
    else:
        print("You lose!")
elif player_choice == '2':
    if computer_choice == 0:
        print("You lose!")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("It's a draw!")



