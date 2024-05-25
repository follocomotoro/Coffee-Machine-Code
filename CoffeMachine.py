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

profit = 0

def is_resources_sufficient(order_ingredients):  # Corregido el nombre de la función
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:  # Cambié >= a >
            print(f"Sorry there is not enough {item}.")  # Usé f-string para la plantilla literal
            return False
    return True

total = 0

def process_coins(total):  # Eliminé el parámetro total, se inicializa dentro de la función
    """Returns el total calculado de monedas"""
    print("Please insert coins.")
    total = 0  # Mover la inicialización de total aquí
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10  # Cambié 0.01 a 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01  # Cambié "pennis" a "pennies"
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return when payment is accepted or false when not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is $ {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")  # Corregido el mensaje
        return False

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ")



is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")  # Cambié comillas dobles a simples
        print(f"Milk: {resources['milk']}ml")  # Cambié comillas dobles a simples
        print(f"Coffee: {resources['coffee']}g")  # Cambié comillas dobles a simples
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resources_sufficient(drink["ingredients"]):  # Cambié el nombre de la función y uso de f-string
            payment = process_coins(total)  # Llamada corregida a la función sin parámetro
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
