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
    "money": 0,
}

STATE = 'on'


def print_report():
    print(f"Water: {resources['water']}ml.")
    print(f'Milk: {resources["milk"]}ml.')
    print(f'Coffee: {resources["coffee"]}gram.')
    print(f'Money: ${resources["money"]}')


def check_resources(coffee):
    global MENU
    global resources
    is_espresso = coffee == 'espresso'
    if is_espresso:
        enough_water = resources["water"] > MENU[coffee]['ingredients']['water']
        enough_coffee = resources["coffee"] > MENU[coffee]['ingredients']['coffee']
    else:
        enough_water = resources["water"] > MENU[coffee]['ingredients']['water']
        enough_coffee = resources["coffee"] > MENU[coffee]['ingredients']['coffee']
        enough_milk = resources["milk"] > MENU[coffee]['ingredients']['milk']
    if enough_water and is_espresso and enough_coffee:
        return True
    elif enough_water and enough_milk and enough_coffee:
        return True
    elif is_espresso:
        if not enough_water:
            print("Sorry there is not enough water.")
        elif not enough_coffee:
            print("Sorry there is not enough coffee.")
        # elif not enough_milk:
        #     print("Sorry there is not enough milk.")
        return False
    else:
        if not enough_water:
            print("Sorry there is not enough water.")
        elif not enough_coffee:
            print("Sorry there is not enough coffee.")
        elif not enough_milk:
            print("Sorry there is not enough milk.")
        return False


def process_coins(coffee):
    print('Please insert coins.')
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money_received = pennies * 0.01 + nickles * 0.05 + dimes * 0.1 + quarters * 0.25
    cost_of_coffee = MENU[coffee]['cost']
    change = money_received - cost_of_coffee
    if money_received < cost_of_coffee:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif change > 0:
        print(f'Here is ${change} in change.')
    return True


def make_coffee(coffee):
    global resources
    global MENU
    if coffee == 'espresso':
        resources["water"] -= MENU[coffee]['ingredients']['water']
        resources["coffee"] -= MENU[coffee]['ingredients']['coffee']
        resources['money'] += MENU[coffee]['cost']
    else:
        resources["water"] -= MENU[coffee]['ingredients']['water']
        resources["coffee"] -= MENU[coffee]['ingredients']['coffee']
        resources["milk"] -= MENU[coffee]['ingredients']['milk']
        resources['money'] += MENU[coffee]['cost']


while STATE == 'on':
    customer_input = input("What would you like? (espresso/latte/cappuccino):")
    if customer_input == 'report':
        print_report()
    elif customer_input == 'off':
        state = 'off'
    elif customer_input == 'espresso' or input == 'latte' or input == 'cappuccino':
        if check_resources(customer_input):
            if process_coins(customer_input):
                make_coffee(customer_input)
                print(f'Here is your {customer_input} Enjoy!')




