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
is_on = True


def resources_check(order_ingredients):
    """Returns True when order can be made"""
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry, not enough {i}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return true when payment accepted."""
    if money_received >= drink_cost:
        reszta = round(money_received - drink_cost, 2)
        print(f"Here is {reszta}$ in change.")
        global money
        money += money_received
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources"""
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your coffee.")


while is_on:
    wybor = input("What would you like? (espresso/latte/cappuccino): ")
    if wybor == "off":
        is_on = False
    elif wybor == "report":
        print('''
    Water: {} ml
    Milk: {} ml
    Coffee: {} g
    Money: {} $
    '''.format(resources.get("water"), resources.get("milk"), resources.get("coffee"), money))
    else:
        drink = MENU[wybor]
        print(drink)
        if resources_check(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(wybor, drink["ingredients"])
