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


def print_report(supply, machine_money):
    print(f"Water: {supply["water"]}ml")
    print(f"Milk: {supply["milk"]}ml")
    print(f"Coffee: {supply["coffee"]}g")
    print(f"Money: ${round(machine_money, 2)}")


def count_coin(change):
    total = 0.0
    total += change["quarters"] * .25
    total += change["dimes"] * .10
    total += change["nickles"] * .05
    total += change["pennies"] * .01
    return total


def check_resources(supply, coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][ingredient] > supply[ingredient]:
            res = [False, ingredient]
            return res
    return [True]


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
run_program = True
profit = 0
while run_program:
    run_coin_slot = True
    money = 0
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }
    choice = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        run_program = False
    elif choice == "report":
        print_report(resources, profit)
    elif choice == 'espresso' or choice == "latte" or choice == "cappuccino":
        # check to see if there are enough resources in machine
        response = check_resources(resources, choice)
        # check_resources returns a list, list[0] (bool) to indicate if there is enough resources
        # and the item it failed on in list[1]
        if response[0]:
            print("Please insert coins.")
            for coin in coins:
                coins[coin] = int(input(f"How many {coin}?: "))
            money = count_coin(coins)
            # check to see if user paid correct amount or more
            if money >= MENU[choice]["cost"]:
                if money != MENU[choice]["cost"]:
                    print(f"Here is ${round(money - MENU[choice]["cost"],2)} in change.")
                profit += MENU[choice]["cost"]
                # take resource cost of coffee out of resource stock
                for item in MENU[choice]["ingredients"]:
                    resources[item] -= MENU[choice]["ingredients"][item]
                print(f"Here is your {choice} ☕ Enjoy!")
            else:
                print("“Sorry that's not enough money. Money refunded")
        else:
            print(f"Sorry there is not enough {response[1]}.")
    else:
        print("Sorry incorrect input try again.")
