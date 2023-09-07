from replit import clear

def add (n1,n2):
    added = n1+n2
    return n1+n2
def minus (n1,n2):
    minused = n1-n2
    return minused
def divide (n1,n2):
    divided = n1/n2
    return divided
def multiply (n1,n2):
    multipled =n1*n2
    return multipled
operations= {"+": add,"-": minus,"*": multiply,"/" :divide}

def main():
    clear()
    while True:
        n1 =float(input("What's your first number? "))
        operation =input("+\n -\n *\n /\n Pick an operation: ")
        n2 =float(input("what's is your second number? "))
        sum = float(operations[operation](n1,n2))
        print(f"{n1} {operation} {n2} = {sum}")
        ask = input(f"Type'y' to continue calculation with {sum} or type'n' to start new calculation or quit type 'q'").lower()
        if ask =="q":
            print("Calculator closing")
            return False
        while ask == "y":
            n1= float(sum)
            operation =input("+\n -\n *\n /\n Pick an operation: ")
            n2 =float(input("what's is your second number? "))
            sum = operations[operation](n1,n2)
            print(f"{n1} {operation} {n2} = {sum}")
            ask = input(f"Type'y' to continue calculation with {sum} or type'n' to start new calculation or quit type 'q'").lower()
        if ask == "n": 
            clear()
        if ask =="q":
            print("Calculator closing")
            return False            

main()