from replit import clear

print("Welcome to the secret auction program")
def bidding(bid_list,name,bid_count):
    bid_list[name] = bid_count

    
    
def auction ():
    bid_list ={}
    price_list =[]  
    name = input("What is your name?")
    bid_count = int(input("What is your bid?"))
    bidding(bid_list,name,bid_count)
    ask = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    clear()
    while ask == "yes":
        name = input("What is your name?")
        bid_count = int(input("What is your bid?"))
        bidding(bid_list,name,bid_count)
        ask = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
        clear()
    for key in bid_list:
        price_list.append(bid_list[key])
        
    max_price =max(price_list)
    max_price_person= {}
    for key in bid_list:
        if bid_list[key] ==  max_price :
            max_price_person[key]=max_price
            print(f"The winner is {key} with a bid o ${max_price}")
    

auction()