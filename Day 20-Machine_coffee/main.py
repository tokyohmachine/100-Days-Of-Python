from menu import MenuItem
from menu_2 import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()    # call by the attributes the method
money_machine = MoneyMachine()
menu = MenuItem('name', 'water', 'milk', 'coffee','cost')
menu_2 = Menu()

continue_coffee = True

while continue_coffee:
    options = menu_2.get_items()
    choice = input(f"What would you like? espresso, latte, cappuccino: ")
    if choice == "off":
        continue_coffee = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu_2.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and \
                money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
