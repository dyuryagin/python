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
    "water": 200,
    "milk": 300,
    "coffee": 100,
    "money" : 0,
}

working_state = True


def check_resources(beverage):
    return_message = ""
    for item in MENU[beverage]['ingredients']:
        if MENU[beverage]['ingredients'][item] > resources[item]:
            return_message += f"Sorry there is not enough {item}.\n"
    return return_message


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def process_resources(beverage, money):
    for resource in MENU[beverage]['ingredients']:
        resources[resource] -= MENU[beverage]['ingredients'][resource]
    resources['money'] += money


def process_money(beverage):
    return_message = ""
    print("please insert coins.")
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))
    all_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if all_money < MENU[beverage]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        pay_money = 0
        if all_money > MENU[beverage]['cost']:
            change = all_money - MENU[beverage]['cost']
            pay_money = all_money - change
            print(f"Here is your change ${change}")
        process_resources(beverage, pay_money)
        print(f"Here is your {beverage}")


while working_state:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        exit(0)
    elif user_input == "report":
        print_report()
    else:
        if check_resources(user_input):
            print(check_resources(user_input))
            continue
        process_money(user_input)


