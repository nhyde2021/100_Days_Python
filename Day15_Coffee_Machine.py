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

def order_coffee():
    """Prompt user for their coffee choice."""
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return selection

def check_resources(order):
    """Check if there are enough resources to make the ordered coffee."""
    insufficiencies = 0
    available = True
    for key in order['ingredients']:
        if order['ingredients'][key] > resources[key]:
            print(f"Insufficient {key}.")
            insufficiencies += 1
    if insufficiencies > 0:
        available = False
        return available
    return available

def collect_payment(order):
    """Collect coins from user and check if enough money was inserted."""
    global money
    print(f"It's gonna be ${order['cost']}, Please insert coins.")
    quarters = input("How many quarters? ")
    dimes = input("How many dimes? ")
    nickels = input("How many nickels? ")
    pennies = input("How many pennies? ")
    money_inserted = 0
    enough = True

    money_inserted += float(quarters) * 0.25 + float(dimes) * 0.1 + float(nickels) * 0.05 + float(pennies) * .01
    change = round(money_inserted - order['cost'], 2)

    if money_inserted < order['cost']:
        print("Insufficient funds. Refund issued.")
        enough = False
        return enough
    else:
        money += order['cost']
        if change > 0:
            print(f"Here is ${change} in change.")
        else:
            print("Exact change, nice!")
    return enough

def make_coffee(order):
    """Deduct the required ingredients from the resources."""
    for key in order['ingredients']:
        resources[key] -= order['ingredients'][key]
    print("Here is your coffee. Enjoy!")

money = 0
machine_on = True

while machine_on:
    
    drink = order_coffee()

    if drink == "off":
        machine_on = False
    elif drink == "report":
        print(f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}\nmoney: ${money}")
    elif drink in MENU.keys():
        drink = MENU[drink]
        is_enough_resources = check_resources(drink)
        if is_enough_resources:
            is_enough_money = collect_payment(drink)
            if is_enough_money:
                make_coffee(drink)

    else:
        print("Invalid selection. Check you spelling and choose again.")
