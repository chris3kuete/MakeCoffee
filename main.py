import sys
from typing import Any

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

machine_on = True

while machine_on:

    coffee_choice = input("What type of coffee are you trying to get? Espresso,Latte,Cappuccino").lower()

    if coffee_choice == 'off':
        machine_on = False

    elif coffee_choice == 'report':
        for i, value in resources.items():
            print("{}: {}".format(i, value))
    elif coffee_choice == 'latte':
        print("Please insert coins")
        quarters = float(input("How many quarters ?"))
        total = quarters * 0.25
        nickel = float(input("how many nickel?"))
        total += nickel * 0.05
        dimes = float(input("how many dimes?"))
        total += dimes * 0.1
        pennies = float(input("How many pennies?"))
        total += pennies * 0.01

        resources['water'] -= 200
        resources['milk'] -= 150
        resources['coffee'] -= 24

        if resources['water'] <= 0 or resources['milk'] <= 0 or resources['coffee'] <= 0:
            print("You dont have enough ingredients !!")
        elif total > MENU['latte']['cost']:
            change = round(total - MENU['latte']['cost'], 2)

            print(f'the change is {change}')
            print("Here is your drink, Thank you for your business!!")
        else:
            print("You don't have enough money for this transaction")
            resources['water'] = 300
            resources['milk'] = 200
            resources['coffee'] = 100

    elif coffee_choice == 'espresso':
        print("Please insert coins")
        quarters = float(input("How many quarters ?"))
        total = quarters * 0.25
        nickel = float(input("how many nickel?"))
        total += nickel * 0.05
        dimes = float(input("how many dimes?"))
        total += dimes * 0.1
        pennies = float(input("How many pennies?"))
        total += pennies * 0.01

        resources['water'] -= 50
        resources['coffee'] -= 18

        if resources['water'] <= 0 or resources['coffee'] <= 0:
            print("You dont have enough ingredients !!")
        elif total > MENU['espresso']['cost']:
            change = round(total - MENU['espresso']['cost'], 2)

            print(f'the change is {change}')
            print("Here is your drink, Thank you for your business!!")
        else:
            print("You don't have enough money for this transaction ")
            resources['water'] = 300
            resources['coffee'] = 100

    elif coffee_choice == 'capuccino':
        print("Please insert coins")
        quarters = float(input("How many quarters ?"))
        total = quarters * 0.25
        nickel = float(input("how many nickel?"))
        total = nickel * 0.05
        dimes = float(input("how many dimes?"))
        total = dimes * 0.1
        pennies = float(input("How many pennies?"))
        total = pennies * 0.01

        resources['water'] -= 250
        resources['milk'] -= 100
        resources['coffee'] -= 24

        if resources['water'] <= 0 or resources['milk'] <= 0 or resources['coffee'] <= 0:
            print("You dont have enough ingredients !!")
        elif total > MENU['espresso']['cost']:
            change = round(total - MENU['latte']['cost'], 2)

            print(f'the change is {change}')
            print("Here is your drink, Thank you for your business!!")
        else:
            print("You don't have enough money for this transaction")
            resources['water'] = 300
            resources['milk'] = 200
            resources['coffee'] = 100



