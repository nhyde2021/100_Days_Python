from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

new_menu = Menu()
machine = CoffeeMaker()
cash_register = MoneyMachine()
turn_off = False

while not turn_off:
    drink = input(f"What would you like? ({new_menu.get_items()}): ")

    if drink == "report":
        machine.report()
        cash_register.report()
        continue
    elif drink == "off":
        turn_off = True
        continue
    else:
        drink = new_menu.find_drink(drink)

        if machine.is_resource_sufficient(drink):
            if cash_register.make_payment(drink.cost):
                machine.make_coffee(drink)


