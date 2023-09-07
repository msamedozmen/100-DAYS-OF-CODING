from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
menu_item = MenuItem
menu = Menu()
# menu_item = MenuItem()
coffee_maker =CoffeeMaker()


#print(coffee_maker.is_resource_sufficient(order))
x = True
while x == True:

    drinks = menu.get_items()
    order =input(f"What would u like {drinks} For checking resources please type 'report' ").lower()
    if order == "report":
        coffee_maker.report()
        money_machine.report()
        report_counter =0
    elif order =="off":
        x=False
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) == True:
            y = drink.cost
            money_machine.make_payment(y)
            coffee_maker.make_coffee(drink)               
                
        
        
