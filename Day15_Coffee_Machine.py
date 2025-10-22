MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
machine_on = True

while machine_on:
    user_selection = input("What would you like? (espresso/latte/cappuccino): ")
    if user_selection == "off":
        machine_on = False
    elif user_selection == "report":
        print(f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}\nmoney: ${money}")
    elif user_selection in MENU.keys():
        user_selection = MENU[user_selection]
        insufficiencies = 0

        for key in user_selection['ingredients']:
            if user_selection['ingredients'][key] > resources[key]:
                print(f"Insufficient {key}.")
                insufficiencies += 1
            else:
                if insufficiencies == 0:
                    resources[key] -= user_selection['ingredients'][key]
        if insufficiencies > 0:
            continue

        quarters = input("How many quarters? ")
        dimes = input("How many dimes? ")
        nickels = input("How many nickels? ")
        pennies = input("How many pennies? ")
        money_inserted = 0

        money_inserted += float(quarters) * 0.25 + float(dimes) * 0.1 + float(nickels) * 0.05 + float(pennies) * .01
        change = round(money_inserted - user_selection['cost'], 2)
        money += money_inserted

        if money_inserted < user_selection['cost']:
            print("Insufficient funds. Refund issued.")
            money -= money_inserted
            for key in user_selection['ingredients']:
                resources[key] += user_selection['ingredients'][key]
        else:
            money -= change
            print(f"Here's your change: ${change}\nEnjoy your coffee!")
    else:
        print("Invalid input. Check your spelling and try again.")