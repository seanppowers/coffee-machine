import machine_templates

ERROR_INSUFFICIENT_RESOURCES = 'Sorry there are not enough resources to make your drink.'
ERROR_INSUFFICIENT_PAYMENT = "Money refunded. Please enter the correct amount of money to purchase your drink."

ESPRESSO_PRICE = machine_templates.MENU.get("espresso").get("cost")
LATTE_PRICE = machine_templates.MENU.get("latte").get("cost")
CAPPUCCINO_PRICE = machine_templates.MENU.get("cappuccino").get("cost")

MACHINE_WATER = machine_templates.resources["water"]
MACHINE_MILK = machine_templates.resources["milk"]
MACHINE_COFFEE = machine_templates.resources["coffee"]

MACHINE_QUARTERS = machine_templates.resources["quarters"]
MACHINE_DIMES = machine_templates.resources["dimes"]
MACHINE_NICKLES = machine_templates.resources["nickles"]

QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKLE_VALUE = 0.05
