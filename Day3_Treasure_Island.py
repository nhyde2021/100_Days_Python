print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is a casino in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the casino with only a dollar. There are 3 slot machines. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("You pull the lever and suddenly die. Game Over.")
        elif choice3 == "blue":
            print("You pull the lever and just some bees come out. Game Over.")
        elif choice3 == "yellow":
            print("JACKPOT! You Win!")
        else:
            print("Bruh, what?. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You get beaten up by a Leprechaun. Game Over.")