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

if player_choice not in ['0', '1', '2']:
    print("Invalid input! Try again.")
    player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

print(f"\nYou chose:\n{options[int(player_choice)]}")

if player_choice == '0':
    
    if computer_choice == 0:
        print(f"Computer chose:\n{options[int(computer_choice)]}\nIt's a draw!")
    elif computer_choice == 1:
        print(f"Computer chose:\n{options[int(computer_choice)]}\nYou lose!")
    else:
        print(f"Computer chose:\n{options[int(computer_choice)]}\nYou win!")

elif player_choice == '1':
    if computer_choice == 0:
        print(f"Computer chose:\n{options[int(computer_choice)]}\nYou win!")
    elif computer_choice == 1:
        print(f"Computer chose:\n{options[int(computer_choice)]}\nIt's a draw!")
    else:
        print(f"Computer chose:\n{options[int(computer_choice)]}\nYou lose!")
elif player_choice == '2':
    if computer_choice == 0:
        print(f"Computer chose:\n{options[int(computer_choice)]}\nYou lose!")
    elif computer_choice == 1:
        print(f"Computer chose:\n{options[int(computer_choice)]}\nYou win!")
    else:
        print(f"Computer chose:\n{options[int(computer_choice)]}\nIt's a draw!")



