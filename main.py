import constants
import machine_templates


def report():
    resources_quarters = constants.MACHINE_QUARTERS
    resources_dimes = constants.MACHINE_DIMES
    resources_nickles = constants.MACHINE_NICKLES
    resources_total_money = (resources_quarters * constants.QUARTER_VALUE) + (resources_dimes * constants.DIME_VALUE) + (resources_nickles * constants.NICKLE_VALUE)

    print("Water: " + str(constants.MACHINE_WATER))
    print("Milk: " + str(constants.MACHINE_MILK))
    print("Coffee: " + str(constants.MACHINE_COFFEE))

    print("Quarters: " + str(constants.MACHINE_QUARTERS))
    print("Dimes: " + str(constants.MACHINE_DIMES))
    print("Nickles: " + str(constants.MACHINE_NICKLES))

    print("Total Money: $" + str(resources_total_money) + "0")

def update_machine_money():
    constants.MACHINE_QUARTERS += int(enter_coins.quarter_input)
    constants.MACHINE_DIMES += int(enter_coins.dime_input)
    constants.MACHINE_NICKLES += int(enter_coins.nickle_input)

def enter_coins():
    enter_coins.customer_money = 0
    enter_coins.customer_quarters = 0
    enter_coins.customer_dimes = 0
    enter_coins.customer_nickles = 0

    enter_coins.quarter_input = input("Enter quarters: ")
    enter_coins.customer_quarters += float(enter_coins.quarter_input) * constants.QUARTER_VALUE
    enter_coins.customer_money += enter_coins.customer_quarters

    enter_coins.dime_input = input("Enter dimes: ")
    enter_coins.customer_dimes += float(enter_coins.dime_input) * constants.DIME_VALUE
    enter_coins.customer_money += enter_coins.customer_dimes

    enter_coins.nickle_input = input("Enter nickles: ")
    enter_coins.customer_nickles += float(enter_coins.nickle_input) * constants.DIME_VALUE
    enter_coins.customer_money += enter_coins.customer_nickles

    return enter_coins.customer_money


def dispense_espresso():
    print("Enjoy your espresso!")
    constants.MACHINE_WATER = constants.MACHINE_WATER - 50
    constants.MACHINE_COFFEE = constants.MACHINE_COFFEE - 18
    update_machine_money()
    user_choice()


def dispense_latte():
    print("Enjoy your latte!")
    constants.MACHINE_WATER = constants.MACHINE_WATER - 200
    constants.MACHINE_MILK = constants.MACHINE_MILK - 150
    constants.MACHINE_COFFEE = constants.MACHINE_COFFEE - 24
    update_machine_money()
    user_choice()


def dispense_cappuccino():
    print("Enjoy your cappuccino!")
    constants.MACHINE_WATER = constants.MACHINE_WATER - 250
    constants.MACHINE_MILK = constants.MACHINE_MILK - 100
    constants.MACHINE_COFFEE = constants.MACHINE_COFFEE - 24
    update_machine_money()
    user_choice()


def user_choice():
    user_input = input('What would you like? (espresso/latte/cappuccino): ')
    if user_input == 'report':
        report()
        user_choice()
    elif user_input == 'off':
        print("SHUTTING DOWN...")
        exit()
    elif user_input == 'espresso':
        if machine_templates.resources["water"] >= 50 and machine_templates.resources["coffee"] >= 18:
            print("Espresso costs " + "$" + str(constants.ESPRESSO_PRICE) + "0")
            enter_coins()
        else:
            print(constants.ERROR_INSUFFICIENT_RESOURCES)
            user_choice()
        if enter_coins.customer_money == constants.ESPRESSO_PRICE:
            dispense_espresso()
            user_choice()
        else:
            print(constants.ERROR_INSUFFICIENT_PAYMENT)
            user_choice()

    elif user_input == 'latte':
        if machine_templates.resources["water"] >= 200 and machine_templates.resources["milk"] >= 150 and \
                machine_templates.resources["coffee"] >= 24:
            print("Latte costs " + "$" + str(constants.LATTE_PRICE) + "0")
            enter_coins()
        else:
            print(constants.ERROR_INSUFFICIENT_RESOURCES)
            user_choice()
        if enter_coins.customer_money == constants.LATTE_PRICE:
            dispense_latte()
            update_machine_money()
            user_choice()
        else:
            print(constants.ERROR_INSUFFICIENT_PAYMENT)
            user_choice()

    elif user_input == 'cappuccino':
        if machine_templates.resources["water"] >= 250 and machine_templates.resources["milk"] >= 100 and \
                machine_templates.resources["coffee"] >= 24:
            print("Cappuccino costs " + "$" + str(constants.CAPPUCCINO_PRICE))
            update_machine_money()
            enter_coins()
        else:
            print(constants.ERROR_INSUFFICIENT_RESOURCES)
            user_choice()
        if enter_coins.customer_money == constants.CAPPUCCINO_PRICE:
            dispense_cappuccino()
            update_machine_money()
            user_choice()
        else:
            print(constants.ERROR_INSUFFICIENT_PAYMENT)
            user_choice()


user_choice()
