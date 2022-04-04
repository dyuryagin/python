from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

working_state = True

while working_state:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        menu_item = menu.find_drink(user_input)
        if menu_item and coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)





