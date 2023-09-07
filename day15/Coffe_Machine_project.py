
from coffe_machine_menu import MENU,resources


def resources_load(water,milk,coffe,money):
    print("Water: ",water)
    print("Milk: ",milk)
    print("Coffe: ",coffe)
    print("Money: ",money)


def coins_calculation(quarters,dimes,nickles,pennies,cost):
    total_coins= (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    change = round(total_coins - cost,2)
    print(f"Here is {change}$ in change")

def macchine_money(quarters,dimes,nickles,pennies,cost):
    total_coins= (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    change = total_coins - cost
    return cost


def resource_checking(ask):
    if ask == "espresso":
        waters=MENU[ask]["ingredients"]["water"]
        coffes = MENU[ask]["ingredients"]["coffee"]
        if resources["water"]< waters  or resources["coffee"]< coffes :
            print("Sorry there is not enough water")
            count=0
        else:
            count=2
            return count
    else:
        waters=MENU[ask]["ingredients"]["water"]
        milks =MENU[ask]["ingredients"]["milk"]
        coffes = MENU[ask]["ingredients"]["coffee"]
        if resources["water"]< waters or resources["milk"]< milks or resources["coffee"]< coffes :
            print("Sorry there is not enough water")
            count=0
        else:
            count=2
            return count
         

def main():
    money=0
    while True:
        second_main =0
        main_count=0

        while main_count<1:
            order =input("What would u like (espresso/cappuccino/latte) For checking resources please type 'report'").lower()
            if order == "report":
                resources_load(resources["water"],resources["milk"],resources["coffee"],money)
                report_counter=0
                while report_counter<1:
                    order =input("What would u like (espresso/cappuccino/latte) For checking resources please type 'report'").lower()
                    new_count=resource_checking(order)
                    if new_count == 2:
                        report_counter =2
                        
                quarters=int(input("How many quarters "))       
                dimes=int(input("How many quarters "))        
                nickles=int(input("How many quarters "))        
                pennies=int(input("How many quarters "))  
                cost = MENU[order]["cost"]
                coins_calculation(quarters,dimes,nickles,pennies,cost)
                macchine_money(quarters,dimes,nickles,pennies,cost)
                money +=cost
                if order == "espresso":
                    resources["water"] =resources["water"] - MENU[order]["ingredients"]["water"]
                    #resources["milk"] = MENU[order]["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"]-MENU[order]["ingredients"]["coffee"]
                    main_count=1
                    second_main=1
                else:  
                    resources["water"] =resources["water"] - MENU[order]["ingredients"]["water"]
                    resources["milk"] =resources["milk"]- MENU[order]["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"]-MENU[order]["ingredients"]["coffee"]
                    main_count=1
                    second_main =1
            else:
                new_count=resource_checking(order)
                if new_count == 2:
                    main_count =2
        while second_main<1:                
            quarters=int(input("How many quarters "))       
            dimes=int(input("How many quarters "))        
            nickles=int(input("How many quarters "))        
            pennies=int(input("How many quarters "))  
            cost = MENU[order]["cost"]
            coins_calculation(quarters,dimes,nickles,pennies,cost)
            macchine_money(quarters,dimes,nickles,pennies,cost)
            money +=cost
            if order == "espresso":
                resources["water"] =resources["water"] - MENU[order]["ingredients"]["water"]
                        #resources["milk"] = MENU[order]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"]-MENU[order]["ingredients"]["coffee"]
                second_main=1
            else:  
                resources["water"] =resources["water"] - MENU[order]["ingredients"]["water"]
                resources["milk"] =resources["milk"]- MENU[order]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"]-MENU[order]["ingredients"]["coffee"]
                
                second_main=1                
main()
 
